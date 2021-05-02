from django import forms
from CRUD.models import billmodel

class cusforms(forms.ModelForm):
    class Meta:
        model=billmodel()
        fields="__all__"