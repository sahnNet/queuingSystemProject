from django import forms
from django.core import validators
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Subject'), 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(limit_value=200, message=_('It can be up to 200 characters')),
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': _('Email'),
                                       'class': 'form-control Input'}),
        validators=[
            validators.EmailValidator(message=_('The entered email is not valid'))
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '3'}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        check_validation_email_list = email.split('@')
        if check_validation_email_list[-1] not in ['gmail.com', 'yahoo.com']:
            raise forms.ValidationError('@gmail.com , @yahoo.com')

        return email
