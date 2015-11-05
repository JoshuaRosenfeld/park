from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime

errors = {'required': 'Required field',}

class SearchForm(forms.Form):
	address = forms.CharField(error_messages=errors, widget=forms.TextInput(attrs={'class': 'form-control no-rad-right', 'id': 'address-input', 'placeholder': 'Where are you going?',}))
	date = forms.DateField(input_formats=['%m/%d/%Y',], error_messages=errors, widget=forms.DateInput(attrs={'class': 'form-control no-rad datepicker', 'placeholder': 'What day?',}))
	time = forms.TimeField(input_formats=['%I:%M %p',], error_messages=errors, widget=forms.TimeInput(attrs={'class': 'form-control no-rad timepicker', 'placeholder': 'What time?',}))