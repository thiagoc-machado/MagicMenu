from rest_framework import viewsets
from .models import Menu, Menu_image, Category
from .serializers import MenuSerializer, MenuImageSerializer, CategorySerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuImageViewSet(viewsets.ModelViewSet):
    queryset = Menu_image.objects.all()
    serializer_class = MenuImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
