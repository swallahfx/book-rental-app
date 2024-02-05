from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Rental

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
        
class RentalSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use the UserSerializer to represent the user field

    class Meta:
        model = Rental
        fields = ['user', 'title', 'rented_date', 'return_date']

