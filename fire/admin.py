from django.contrib import admin

from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username","first_name", "last_name", "sub_end_date", )
