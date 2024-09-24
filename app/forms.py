from django import forms
from .models import GetInTouch

class GetInTouchForm(forms.ModelForm):

    class Meta:
        model = GetInTouch
        fields  = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Phone', 'value': '998'}),
            'message': forms.Textarea(attrs={'placeholder': 'Project details'}),
        }