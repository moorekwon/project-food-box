from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'nickname', 'gender', 'birth',)
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_admin', 'is_active',)
        })
    )

    list_display = ['email', 'nickname', 'gender', 'birth', 'date_created']
    search_fields = ('email', 'nickname', 'gender',)
    ordering = ('date_created',)
