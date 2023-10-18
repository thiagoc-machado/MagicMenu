from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    age = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip = models.IntegerField(null=True)
    country = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.CharField(max_length=30, null=True)
    updated_by = models.CharField(max_length=30, null=True)
    deleted_by = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=50, null=True)
    notes = models.TextField(null=True)
    photo = models.ImageField(upload_to='clients', null=True)

    def __str__(self):
        return self.name
    

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
