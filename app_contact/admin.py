from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'text']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactUsAdmin)
