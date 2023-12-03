from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.CharField(max_length=30, null=True, blank=True)
    updated_by = models.CharField(max_length=30, null=True, blank=True)
    deleted_by = models.CharField(max_length=30, null=True, blank=True)
    active = models.BooleanField(default=True)
    nutrition_score = models.FloatField(null=True, blank=True)
    nutrition_grade = models.CharField(max_length=1, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    gluten = models.BooleanField(default=False, null=True, blank=True)
    lactose = models.BooleanField(default=False, null=True, blank=True)
    allergens = models.TextField(null=True, blank=True)
    allergen = models.BooleanField(default=False, null=True, blank=True)
    vegan = models.BooleanField(default=False, null=True, blank=True)
    vegetarian = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return self.name

class Menu_image(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_image')

    def __str__(self):
        return str(self.menu)

    
class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

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


    