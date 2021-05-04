from django import forms
from .models import Msg

class MsgForm(forms.ModelForm):
    class Meta:
        model = Msg
        fields = ('message', 'password', 'user')

class IdForm(forms.Form):
    id_usr = forms.CharField()

class PswdForm(forms.ModelForm):
    class Meta:
        model = Msg
        fields = ('password',)