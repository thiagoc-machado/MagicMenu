from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=30, null=True)
    number = models.IntegerField(null=True)
    number_chairs = models.IntegerField(null=True)
    description = models.TextField(null=True)
    type = models.CharField(max_length=30, null=True)
    is_available = models.BooleanField(default=True)
    is_reserved = models.BooleanField(default=False)
    is_occupied = models.BooleanField(default=False)
    is_clean = models.BooleanField(default=True)
    is_broken = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.CharField(max_length=30, null=True)
    updated_by = models.CharField(max_length=30, null=True)
    deleted_by = models.CharField(max_length=30, null=True)

class Seat(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    chair_number = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)
    type = models.CharField(max_length=30, null=True)
    qr_code = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)

def created_at (self):
    return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

def updated_at (self):
    return self.updated_at.strftime('%Y-%m-%d %H:%M:%S')

def deleted_at (self):
    return self.deleted_at.strftime('%Y-%m-%d %H:%M:%S')

def created_by (self):
    return self.created_by

def updated_by (self):
    return self.updated_by

def deleted_by (self):
    return self.deleted_by


# Create your models here.
