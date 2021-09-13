from django import forms
from . import models


class Cash_form(forms.ModelForm):
    class Meta:
        model = models.Cash
        fields = '__all__'

