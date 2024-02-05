# book_rental/models.py

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    page_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    rented_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} rented |{self.title}| to return on  {self.return_date}"


