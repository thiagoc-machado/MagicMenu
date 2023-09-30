from django.contrib import admin


from .models import *

admin.site.register(Menu)
admin.site.register(Menu_ingredient)
admin.site.register(Menu_image)
admin.site.register(Menu_allergene)
admin.site.register(Category)