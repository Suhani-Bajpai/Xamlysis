from django.contrib import admin
#from database.models import sample
from database.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#for entering the data in the admin module
#admin.register(sample)

from .forms import MyUserCreationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ['email_id']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ( """'mobile_number', 'birth_date'""")}),
    ) #this will allow to change these fields in admin module

admin.site.register(User , UserAdmin)

#@admin.register(class_stu_tech)
"""
class UserAdmin(admin.ModelAdmin):
    list_display=('class_stu_tech' )
"""


