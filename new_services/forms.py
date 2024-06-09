from django import forms
from .models import NewAPI


class AddApiForm(forms.ModelForm):
    class Meta:
        model = NewAPI
        exclude = ['user', 'created_at', 'status']
