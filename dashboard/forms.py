from django import forms 
from dashboard.models import NewAnime


class ContactUs(forms.Form):
	full_name = forms.CharField(label= 'first_name', max_length=200)	
	description = forms.CharField(label= 'password', max_length=200)
	email = forms.EmailField(label = 'email')