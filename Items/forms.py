from django import forms
from django.forms import ModelForm

from .models import *

class TasksForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    time = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter an integer between 1 and 10...'}))
    class Meta:
        model = Task
        exclude = ['coin_value']

class UserForm(forms.ModelForm):
    userid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your 7 digit code...'}))
    class Meta:
        model = User
        exclude = ['items', "links"]
