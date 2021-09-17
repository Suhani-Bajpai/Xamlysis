from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from database.models import *
from django.core import validators

class MyUserCreationForm(UserCreationForm):
    email_id = forms.EmailField(max_length=200 )
    

    class Meta(UserCreationForm):
        model = User
        fields = ('email_id', 'username' , 'first_name' , 'last_name','mobile_no' ,)
        #widgets={
        #    'email_id' : forms.EmailInput(attrs={'class':'form-control'}),
        #}

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email_id',)

class class_stu_tech_form(forms.ModelForm):
    class Meta:
        model = class_stu_tech
        fields= ('class_stu_tech' , )
        #widgets={
        #    'class_stu_tech' : forms.TextInput(attrs={'class':'form-control'}),
        #}