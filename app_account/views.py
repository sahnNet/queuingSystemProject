from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from app_contact.models import ContactUs
from app_appointment.models import Appointment
from .forms import (LoginForm,
                    RegisterForm,
                    )


def account_view(request):
    if not request.user.is_authenticated:
        return redirect((reverse('homeView')))

    turns_list = Appointment.objects.filter(user_id=request.user.id)

    # Account page information's
    context = {
        'myTurns': _('My turns'),
        'row': _('Row'),
        'shift': _('Shift'),
        'turn': _('Turn'),
        'doctor': _('Doctor'),
        'medicalCenter': _('Medical center'),
        'province': _('Province'),
        'city': _('City'),
        'date': _('Date'),
        'time': _('Time'),
        'turnFile': _('Turn file'),
        'turnsList': turns_list,
    }
    return render(request, 'account/userPanel.html', context=context)


def account_conversation_view(request):
    if not request.user.is_authenticated:
        return redirect((reverse('homeView')))
    user_email = request.user.email
    conversation_list = ContactUs.objects.filter(email=user_email).all()

    # Account conversation page information's
    context = {
        'email': _('Email'),
        'userEmail': user_email,
        'conversationList': conversation_list,
    }
    return render(request, 'account/userConversation.html', context=context)


def account_card_view(request):
    if not request.user.is_authenticated:
        return redirect((reverse('homeView')))
    # Account card information's
    context = {
        'dashboard': _('Dashboard'),
        'myAccount': _('My account'),
        'myConversations': _('My conversations'),
        'wallet': _('Wallet'),
        'myTurns': _('My turns'),
        'exit': _('Exit'),
    }
    return render(request, 'account/userCard.html', context=context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect((reverse('homeView')))

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            # Successful login
            login(request, user)
            # /Successful login
            return redirect((reverse('homeView')))
        else:
            # Failed login
            login_form.add_error('user_name', _('No user with this name was found'))
            # /Failed login

    # Login page information's
    context = {
        'title': _('Experience easy appointments with us'),
        'login': _('Login'),
        'loginForm': login_form,
        'enter': _('Enter'),
        'rememberMe': _('Remember me'),
        'forgotPassword': _('Forgot your password?'),

    }
    return render(request, 'account/login.html', context=context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect((reverse('homeView')))
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        # Creat an object of User
        user_name = register_form.cleaned_data.get('user_name_code')
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=user_name, email=email, password=password, first_name=first_name,
                                 last_name=last_name)
        # /Creat an object of User
        return redirect((reverse('registerView')))

    # Register page information's
    context = {
        'registerForm': register_form,
        'register': _('Register'),
    }
    return render(request, 'account/registration.html', context=context)


def logout_view(request):
    logout(request)
    return redirect((reverse('homeView')))
