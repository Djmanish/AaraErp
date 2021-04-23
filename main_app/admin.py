from django.contrib import admin
from main_app.models import *

# Register your models here.
class Levels_admin(admin.ModelAdmin):
    list_display  = ('level_name', 'id')

class Role_admin(admin.ModelAdmin):
    list_display  = ('user', 'role_level', 'id',)

admin.site.register(Levels, Levels_admin)
admin.site.register(Role, Role_admin)
