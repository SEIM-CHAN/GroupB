from django import forms
from .models import Board
from .models import Coment

class BoardCreateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title',)

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)





class ComentCreateForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('coment',)

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)