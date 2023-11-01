from rest_framework import viewsets
from .models import Menu, Menu_image, Category
from .serializers import MenuSerializer, MenuImageSerializer, CategorySerializer
from .permissions import IsAdminPermission

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # Aplique a permissão IsAuthenticatedOrReadOnly
    permission_classes = [IsAuthenticatedOrReadOnly]

class MenuImageViewSet(viewsets.ModelViewSet):
    queryset = Menu_image.objects.all()
    serializer_class = MenuImageSerializer

    # Aplique a permissão IsAuthenticatedOrReadOnly
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Aplique a permissão IsAuthenticatedOrReadOnly
    permission_classes = [IsAuthenticatedOrReadOnly]

