from django import forms
from django.core.mail import EmailMessage
from .models import NiceThread

class NiceThreadNewForm(forms.ModelForm):
    class Meta:
        model = NiceThread
        fields = ('title',)
        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)
            pass