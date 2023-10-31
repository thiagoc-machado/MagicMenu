from django.contrib import admin
from .models import Menu, Menu_image, Category

class MenuImageInline(admin.TabularInline):  # Ou admin.StackedInline para uma exibição mais detalhada
    model = Menu_image
    extra = 1  # O número de formulários em branco exibidos para adicionar novas imagens

class CategoryInline(admin.TabularInline):  # Ou admin.StackedInline para uma exibição mais detalhada
    model = Category
    extra = 1  # O número de formulários em branco exibidos para adicionar novas categorias

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'active', 'nutrition_score')
    list_filter = ('type', 'active', 'allergen', 'gluten', 'lactose')
    search_fields = ('name',)
    inlines = [MenuImageInline, CategoryInline]

admin.site.register(Menu, MenuAdmin)
