from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'is_active', 'role',)
    list_filter = ('is_active', 'role')
    search_fields = ('first_name', 'last_name',)


