from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  # Ou admin.StackedInline para uma exibição mais detalhada
    model = OrderItem
    extra = 1  # O número de formulários em branco exibidos para adicionar novos itens

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'employee', 'date', 'status', 'total', 'payment_status')
    list_filter = ('status', 'payment_status')
    search_fields = ('client__name', 'employee__name')
    date_hierarchy = 'date'
    inlines = [OrderItemInline]  # Adicione a classe OrderItemInline aqui

admin.site.register(Order, OrderAdmin)
