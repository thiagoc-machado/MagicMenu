from django.db import models
from clients.models import Client
from tables.models import Table, Seat
from menu.models import Menu
from orders.models import Order

class Finance(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

# Create your models here.
