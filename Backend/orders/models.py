from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from clients.models import Client
from django.contrib.auth.models import User
from menu.models import Menu
from employee.models import Employee
from tables.models import Table, Seat




class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    tip = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_total = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.client.name
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.order.client.name
    
@receiver(pre_save, sender=OrderItem)
def update_order_total(sender, instance, **kwargs):
    order = instance.order
    order.total = OrderItem.objects.filter(order=order).aggregate(models.Sum('total'))['total__sum'] or 0
    order.save()

