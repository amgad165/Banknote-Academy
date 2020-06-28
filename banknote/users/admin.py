from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import  UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['pk','username','email','Role','phone_number','Academic_Year','College','University']
    list_editable=['Role']

    # fieldsets = (
    #     ('Pesrsonal info', {
    #         'fields': ('username','email','Role','phone_number','Academic_Year','College','University')
    #     }),
    #
    # )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
