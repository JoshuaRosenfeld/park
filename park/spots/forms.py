from django import forms
from django.forms.extras.widgets import SelectDateWidget

errors = {'required': 'Required',}

class BookForm(forms.Form):
	address = forms.CharField(error_messages=errors, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address-input', 'placeholder': 'Adddress',}),)
	from_date = forms.DateField(input_formats=['%m/%d/%Y',], error_messages=errors, widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'from-date', 'placeholder': 'Arrival',}),)
	from_time = forms.TimeField(input_formats=['%I:%M %p',], error_messages=errors, widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'id': 'from-time', 'placeholder': 'Time',}),)
	to_date = forms.DateField(input_formats=['%m/%d/%Y',], error_messages=errors, widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'id': 'to-date', 'placeholder': 'Departure',}),)
	to_time = forms.TimeField(input_formats=['%I:%M %p',], error_messages=errors, widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'id': 'to-time', 'placeholder': 'Time',}),)

	def clean(self):
		cleaned_data = super(BookForm, self).clean()
		from_date = cleaned_data.get("from_date")
		from_time = cleaned_data.get("from_time")
		to_date = cleaned_data.get("to_date")
		to_time = cleaned_data.get("to_time")

		if to_date and from_date:
			if to_date < from_date:
				msg = 'Error: end date must follow start date'
				self.add_error(None, msg)
			elif to_date == from_date:
				if to_time and from_time:
					if to_time < from_time:
						msg = 'Error: end time must follow start time'
						self.add_error(None, msg)

		return self.cleaned_data

	def __init__(self, *args, **kwargs):
		should_glue = kwargs.pop('should_glue')
		super(BookForm, self).__init__(*args, **kwargs)

		if should_glue:	
			self.fields['address'].widget.attrs['class'] += ' no-rad-right'
			self.fields['from_date'].widget.attrs['class'] += ' no-rad'
			self.fields['from_time'].widget.attrs['class'] += ' no-rad'
			self.fields['to_date'].widget.attrs['class'] += ' no-rad'
			self.fields['to_time'].widget.attrs['class'] += ' no-rad'
		else:
			self.fields['from_date'].widget.attrs['class'] += ' no-rad-right'
			self.fields['from_time'].widget.attrs['class'] += ' no-rad-left'
			self.fields['to_date'].widget.attrs['class'] += ' no-rad-right'
			self.fields['to_time'].widget.attrs['class'] += ' no-rad-left'
	