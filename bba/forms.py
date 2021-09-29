from django import forms
from .models import Comment, Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ("subject",)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "message",)