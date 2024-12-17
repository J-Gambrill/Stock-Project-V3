from django import forms 
from . import models

class CreateRequest(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['name', 'amount', 'description', 'importance', 'banner']