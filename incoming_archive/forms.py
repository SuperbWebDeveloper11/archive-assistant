from django import forms
from .models import Mail



class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('registration_number', 'reference_number', 'source', 'title', 'pdf_copy')

