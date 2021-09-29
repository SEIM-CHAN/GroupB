from django import forms
from .models import Thread, Comment


class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ("title", "exp")

        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)

        def __init__(self, *args, **kwargs):
            super().__init__( *args, **kwargs)


