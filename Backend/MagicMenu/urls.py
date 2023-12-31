from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions

from menu.viewsets import MenuViewSet
from users.viewsets import UserViewSet
from rest_framework_simplejwt.views import TokenVerifyView

router = routers.DefaultRouter()
router.register(r'items-cardapio', MenuViewSet)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="MagicMenu API",
        default_version='v1',
        description="Magic Menu",
        terms_of_service="https://www.magicmenu.com/termos",
        contact=openapi.Contact(email="magicmenu@magicmenu.com"),
        license=openapi.License(name="Direitos reservados"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list'),
    path('api/users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
