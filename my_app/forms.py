from django import forms
from .models import Brewing

class BrewingForm(forms.ModelForm):
    class Meta:
        model = Brewing
        fields = ['date', 'temperature', 'steeping_time', 'amount', 'water_amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'temperature': forms.NumberInput(attrs={'min': 0, 'max': 212}),
            'steeping_time': forms.TextInput(attrs={'placeholder': 'e.g., 3 minutes'}),
            'amount': forms.NumberInput(attrs={'min': 0}),
            'water_amount': forms.NumberInput(attrs={'min': 0}),
        }