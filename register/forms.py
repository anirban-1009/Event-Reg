from django import forms
from django.utils import timezone
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'age', 'number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Name'}),
            'age': forms.DateTimeInput(attrs={'class': 'form-control rounded', 'placeholder': 'Age'}),
            'number': forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'Mobile Number'}),
        }
