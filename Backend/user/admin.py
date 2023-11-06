from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

# Desregistre o UserAdmin padrão
admin.site.unregister(User)
# Registre o UserAdmin personalizado
admin.site.register(User, CustomUserAdmin)
