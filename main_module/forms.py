from django import forms
from .models import add_comments ,contact,order_data



class comments(forms.ModelForm):
    class Meta:
        model=add_comments
        fields=('email','text',)

class contact_form(forms.ModelForm):
    class Meta:
        model= contact
        fields=('email','name','text',)



class order_detail_form(forms.ModelForm):
    class Meta:
        model=order_data
        fields=('__all__')