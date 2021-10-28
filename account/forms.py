from django import forms
from django.forms import widgets

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length = 100, widget=forms.PasswordInput())

class CSVUploadForm(forms.Form):
    delimiter = forms.CharField(max_length = 1)
    csv_file = forms.FileField()