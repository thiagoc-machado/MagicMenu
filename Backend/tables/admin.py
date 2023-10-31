from django.contrib import admin
from .models import Table, Seat

class SeatInline(admin.TabularInline):  # Ou admin.StackedInline para uma exibição mais detalhada
    model = Seat
    extra = 1  # O número de formulários em branco exibidos para adicionar novos assentos

class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'number_chairs', 'is_available', 'is_reserved', 'is_occupied', 'is_clean', 'is_broken')
    list_filter = ('is_available', 'is_reserved', 'is_occupied', 'is_clean', 'is_broken')
    search_fields = ('name',)
    inlines = [SeatInline]

admin.site.register(Table, TableAdmin)
