from django.contrib import admin
from .models import User, PermissionsMixin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .form import UserChangeForm, UserCreationForm


class UserAdminSite(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['username', 'email', 'is_active']
    list_filter = ('is_admin', )

    fieldsets = (
        (None, {'fields': ('username', 'password', 'last_login')}),
        ('personal_info', {'fields': ('first_name', 'last_name', 'phone_number', 'email', 'age', 'gender')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'user_permissions', 'groups')})
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'phone_number', 'password1', 'password2')}),
    )

    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    filter_horizontal = ('user_permissions', 'groups')


admin.site.unregister(Group)
admin.site.register(User, UserAdminSite)


