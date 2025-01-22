from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role') 
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('role',)

admin.site.register(User, UserAdmin)
