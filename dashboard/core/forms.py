from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  organization = forms.CharField(max_length=128)

  class Meta(UserCreationForm.Meta):
    model = User
    fields = ('username', 'organization', 'password1', 'password2')