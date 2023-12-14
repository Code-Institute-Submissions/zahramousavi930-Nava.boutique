from django import forms
from .models import add_comments ,contact



class comments(forms.ModelForm):
    class Meta:
        model=add_comments
        fields=('email','text',)

class contact_form(forms.ModelForm):
    class Meta:
        model= contact
        fields=('email','name','text',)