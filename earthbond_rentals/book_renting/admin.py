from django.contrib import admin
from .models import User, Book, Rental

admin.site.register(Book)
admin.site.register(Rental)


