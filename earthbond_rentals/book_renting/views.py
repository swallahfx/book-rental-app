from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Rental, Book
from django.contrib.auth.models import User
from .serializers import RentalSerializer, UserSerializer, BookSerializer
from .utils import fetch_book_details


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def calculate_fee(self, page_number, rented_date, return_date):
        remaining_days = max(0, (return_date - rented_date).days - 30)
        paying_days = remaining_days / 30
        fee = round((page_number / 100) * paying_days, 2)
        return fee

    def perform_create(self, serializer):
        user_id = serializer.validated_data['user']
        title = serializer.validated_data['title']
        return_date = serializer.validated_data['return_date']
        rented_date = serializer.validated_data['rented_date']

        user_exists = User.objects.filter(id=user_id).first()
        if user_exists:
            book_exists = Book.objects.filter(title=title).first()
            if not book_exists:
                book_data = {'title': title}
                BookViewSet().perform_create(BookSerializer(data=book_data))
                book_exists = Book.objects.filter(title=title).first()
                if not book_exists.page_number:
                    return Response({"error": "Number of pages in Book cannot be Zero"}, status=status.HTTP_400_BAD_REQUEST)

            fee = self.calculate_fee(book_exists.page_number, rented_date, return_date)

            response = {
                "book_borrowed": title,
                "borrower_name": user_exists.name,
                "borrowing_fee": fee,
                "return_date": return_date
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({"error": "You are not registered yet"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        instance = serializer.instance
        title = instance.title.title
        return_date = serializer.validated_data['return_date']
        rented_date = instance.rented_date

        book_exists = Book.objects.filter(title=title).first()
        if not book_exists:
            return Response({"error": "Book not found"}, status=status.HTTP_400_BAD_REQUEST)

        fee = self.calculate_fee(book_exists.page_number, rented_date, return_date)

        instance.fee = fee
        instance.save()

        return Response({"status": "Rental updated successfully"}, status=status.HTTP_200_OK)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        number_of_pages = fetch_book_details(title)

        Book.objects.create(title=title, page_number=number_of_pages)

        return Response({'number_of_pages': number_of_pages}, status=status.HTTP_201_CREATED)
