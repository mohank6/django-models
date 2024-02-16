from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Passport(models.Model):
    passport_number = models.CharField(max_length=9)
    country = models.CharField(max_length=50)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

