from django.db import models

# Create your models here.
class MenuItem(models.Model):
    ID = models.IntegerField
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField
    def __str__(self):
        return f'{self.title}:{str(self.price)}'

class Booking(models.Model):
    ID = models.IntegerField
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField
    BookingDate = models.DateTimeField()

class User(models.Model):
    ID = models.IntegerField
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField
    BookingDate = models.DateTimeField()
