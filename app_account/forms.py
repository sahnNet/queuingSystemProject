from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Enter your username'),
                                      'class': 'form-control',
                                      }),
        label=_('user name')
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('Enter your password'),
                                          'class': 'form-control',
                                          }),
        label=_('password')
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist_user = User.objects.filter(username=user_name).exists()
        if not is_exist_user:
            raise forms.ValidationError(_('Username not found'))

        return user_name


class RegisterForm(forms.Form):
    user_name_code = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': _('National Code'),
                                        'class': 'form-control'}),
        label=_('National Code'),
        validators=[
            validators.MaxLengthValidator(limit_value=10, message=_('It can be up to 10 characters')),
            validators.MinLengthValidator(limit_value=10, message=_('Must be at least 10 characters')),
        ]
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('First name'),
                                      'class': 'form-control'}),
        label=_('First name'),
        validators=[
            validators.MaxLengthValidator(limit_value=50, message=_('It can be up to 50 characters')),
            validators.MinLengthValidator(limit_value=1, message=_('Must be at least 1 characters')),
        ]
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Last name'),
                                      'class': 'form-control'}),
        label=_('Last name'),
        validators=[
            validators.MaxLengthValidator(limit_value=50, message=_('It can be up to 50 characters')),
            validators.MinLengthValidator(limit_value=1, message=_('Must be at least 1 characters')),
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': _('Email'),
                                       'class': 'form-control'}),
        label=_('Email'),
        validators=[
            validators.EmailValidator(message=_('The entered email is not valid'))
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('password'),
                                          'class': 'form-control'}),
        label=_('password'),
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('Repeat the password'),
                                          'class': 'form-control'}),
        label=_('Repeat the password'),
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist_user = User.objects.filter(username=user_name).exists()
        if is_exist_user:
            raise forms.ValidationError(_('This username is already registered'))

        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist_email = User.objects.filter(email=email).exists()

        check_validation_email_list = email.split('@')
        if check_validation_email_list[-1] not in ['gmail.com', 'yahoo.com']:
            raise forms.ValidationError('@gmail.com , @yahoo.com')

        if is_exist_email:
            raise forms.ValidationError(_('This email is already registered'))

        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError(_('Password and its repetition are not equal'))
        return password
