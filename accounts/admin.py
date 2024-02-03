from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ( 'id','name', 'email', 'gender', 'phone_num', 'account', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone_num', 'gender', 'account' )}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'name', 'phone_num', 'gender', 'account', 'password1', 'password2'
                )
            }
        ),
    )
    ordering = ('name', 'account')

admin.site.register(CustomUser, CustomUserAdmin)


