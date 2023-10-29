from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    age = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.CharField(max_length=30, null=True, blank=True)
    updated_by = models.CharField(max_length=30, null=True, blank=True)
    deleted_by = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
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
