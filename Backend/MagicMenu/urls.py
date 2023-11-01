
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from menu.viewsets import MenuViewSet

router = routers.DefaultRouter()
router.register(r'itens-cardapio', MenuViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/itens-cardapio/', include(router.urls)),
    path('api/itens-cardapio/new/', MenuViewSet.as_view({'post': 'create'})),
    path('api/itens-cardapio/<int:pk>/', MenuViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
