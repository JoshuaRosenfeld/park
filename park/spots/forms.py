from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime

class SearchForm(forms.Form):
	address = forms.CharField(required=True)
	date = forms.DateField(required=True, widget=SelectDateWidget(), initial=datetime.date.today)
	time = forms.TimeField()
