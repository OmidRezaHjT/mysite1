from django import forms
from website.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'
    