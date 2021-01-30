from django import forms
from . import models

class Creden(forms.ModelForm):
    class Meta:
        model = models.credentails
        fields=['cc','email','phone','address','zip_code' ]