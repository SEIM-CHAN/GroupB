from django import forms
from django.core.mail import EmailMessage
from .models import NiceThread, NiceComment

class NiceThreadCreateForm(forms.ModelForm):
    class Meta:
        model = NiceThread
        fields = ('title', 'desc',)
        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)

class NiceCommentUpdateForm(forms.ModelForm):
    class Meta:
        model = NiceComment
        fields = ()
        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)

class NiceCommentCreateForm(forms.ModelForm):
    class Meta:
        model = NiceComment
        fields = ('text',)
        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)
