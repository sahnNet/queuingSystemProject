from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))
    email = models.EmailField(max_length=100, verbose_name=_('Email'))
    text = models.TextField(verbose_name=_('Message'))
    is_read = models.BooleanField(default=False, verbose_name=_('Read / Unread'))

    class Meta:
        verbose_name = _('Contact users')
        verbose_name_plural = _('User calls')

    def __str__(self):
        return self.subject
