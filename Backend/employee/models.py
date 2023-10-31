from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True,blank=True)
    photo = models.ImageField(upload_to='employee', null=True)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.CharField(max_length=30, null=True)
    updated_by = models.CharField(max_length=30, null=True)
    deleted_by = models.CharField(max_length=30, null=True)


# Create your models here.
