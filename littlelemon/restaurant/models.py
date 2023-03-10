from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name + ' ' + f"{self.number:.2f}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f"{self.title} : {self.price:.2f}"
