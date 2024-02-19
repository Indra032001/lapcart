from django import forms
from .models import Laptop


class cartForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
