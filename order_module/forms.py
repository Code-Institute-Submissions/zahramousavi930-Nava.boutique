
from django import forms
from .models import order_data








class order_detail_form(forms.ModelForm):
    class Meta:
        model=order_data
        fields=('full_name',
                'email_address',
                'phone_number',
                'street_address1',
                'town_or_city',
                'country_state_or_location',
                'post_code',
                'country')
