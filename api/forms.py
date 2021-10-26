from django import forms
from django.forms import fields
from .models import Candidate

class VoteCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['']