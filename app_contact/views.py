from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm
from .models import ContactUs


def contactus_view(request):
    contact_form = ContactForm(request.POST or None)

    if contact_form.is_valid():
        # Creat an object of ContactUs
        subject = contact_form.cleaned_data.get('subject')
        email = contact_form.cleaned_data.get('email')
        text = contact_form.cleaned_data.get('text')

        ContactUs.objects.create(subject=subject, email=email, text=text)

        contact_form = ContactForm(None)
        # /Creat an object of ContactUs
    # Contact us information's
    context = {
        'formContact': contact_form,
        'contactus': _('Contact us'),
        'send': _('send'),
    }

    return render(request, 'contact.html', context)
