from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('introduction','link','icon','birthday',)}),)
    list_display = ['username', 'email','introduction','link','icon','birthday']

admin.site.register(CustomUser, CustomUserAdmin)