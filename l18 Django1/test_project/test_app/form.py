from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):

    name = forms.CharField()
    message = forms.CharField()
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <=3:
            raise ValidationError('Too few letters')
        return name

    def clean(self):
        if self.cleaned_data.get('name', None) == 'Kirill':
            raise ValidationError("Nooo!")
        return self.cleaned_data