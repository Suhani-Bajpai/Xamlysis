from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    email_id = forms.EmailField(max_length=200 )

    class Meta(UserCreationForm):
        model = User
        fields = ('email_id',)

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email_id',)