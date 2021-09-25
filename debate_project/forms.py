from django import forms 

from .models import Evidence

class EvidenceList(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title:'
            }))
    description = forms.CharField(
            label= '',
        widget=forms.Textarea(
            attrs={
                'class': 'new class name',
                'placeholder': 'ToDo:',
                'rows': '5',
                'cols': 80
            }))

    class Meta:
        model = Evidence
        fields = [
            'title',
            'description',
            # 'date'
        ]

