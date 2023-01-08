from django.contrib import admin
from .models import UserInfo

# Register your models here.

@admin.register(UserInfo)
class UserInfoModel(admin.ModelAdmin):
    list_display = ['fname','lname','qualification','contact','email','address']
