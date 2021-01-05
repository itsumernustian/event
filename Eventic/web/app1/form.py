from django import forms
from .models import Contact , Register


class ContactData(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class RegisteredUser(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
