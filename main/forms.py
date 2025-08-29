from django import forms
from .models import FoodDonation

class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = ['food_name', 'quantity', 'expiry_time', 'location', 'photo','phone_number']
        widgets = {
            'expiry_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class DeliveryConfirmationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = ['delivery_photo']
