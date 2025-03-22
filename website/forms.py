from django import forms
from website.models import *
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'
    