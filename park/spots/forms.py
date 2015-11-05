from django import forms
from django.forms.extras.widgets import SelectDateWidget

errors = {'required': 'Required',}

class SearchForm(forms.Form):
	address = forms.CharField(error_messages=errors, widget=forms.TextInput(attrs={'class': 'form-control no-rad-right', 'id': 'address-input', 'placeholder': 'Where are you going?',}),)
	from_date = forms.DateField(input_formats=['%m/%d/%Y',], error_messages=errors, widget=forms.DateInput(attrs={'class': 'form-control no-rad datepicker', 'placeholder': 'What day?',}),)
	from_time = forms.TimeField(input_formats=['%I:%M %p',], error_messages=errors, widget=forms.TimeInput(attrs={'class': 'form-control no-rad timepicker', 'placeholder': 'What time?',}),)

class SearchFormExtended(forms.Form):
	address = forms.CharField(error_messages=errors, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address-input', 'placeholder': 'Adddress',}),)
	from_date = forms.DateField(input_formats=['%m/%d/%Y',], error_messages=errors, widget=forms.DateInput(attrs={'class': 'form-control no-rad-right datepicker', 'placeholder': 'Start date',}),)
	from_time = forms.TimeField(input_formats=['%I:%M %p',], error_messages=errors, widget=forms.TimeInput(attrs={'class': 'form-control no-rad-left timepicker', 'placeholder': 'Start time',}),)
	to_date = forms.DateField(required=False, input_formats=['%m/%d/%Y',], error_messages=errors, widget=forms.DateInput(attrs={'class': 'form-control no-rad-right datepicker', 'placeholder': 'End date',}),)
	to_time = forms.TimeField(required=False, input_formats=['%I:%M %p',], error_messages=errors, widget=forms.TimeInput(attrs={'class': 'form-control no-rad-left timepicker', 'placeholder': 'End time',}),)