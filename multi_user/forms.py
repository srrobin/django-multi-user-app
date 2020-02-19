from django import forms
from .models import memory

class DiaryForm(forms.ModelForm):

    class Meta:
        model = memory
        fields = '__all__'

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control','rows':4, 'cols': 10}),
            'color': forms.Select(attrs={'class': 'form-control'})
        }