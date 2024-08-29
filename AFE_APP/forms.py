from django import forms
from .models import AFE_REQUEST

class MyModelForm(forms.ModelForm):
    class Meta:
        model = AFE_REQUEST
        fields = '__all__'
