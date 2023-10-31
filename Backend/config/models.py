from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=30, null=True)
    logo = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.CharField(max_length=30, null=True)
    updated_by = models.CharField(max_length=30, null=True)
    deleted_by = models.CharField(max_length=30, null=True)

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
