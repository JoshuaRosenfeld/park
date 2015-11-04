from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime

class SearchForm(forms.Form):
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control no-rad-right', 'placeholder': 'Where are you going',}))
	date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control no-rad', 'id': 'datepicker', 'placeholder': 'What day?',}))
	time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control no-rad', 'id': 'timepicker', 'placeholder': 'What time?',}))