from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'Address_line_1',
            'Address_line_2',
            'City',
            'Country',
            'State',
            'Postal_code',
        ]
