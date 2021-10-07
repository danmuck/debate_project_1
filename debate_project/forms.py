from django import forms
from django.forms.widgets import URLInput 

from .models import Evidence

class EvidenceList(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Point:',
                'rows': 2,
                'cols': 60,
            }))
    description = forms.CharField(
        label= '',
        widget=forms.Textarea(
            attrs={
                'class': 'Evidence',
                'placeholder': 'Evidence:',
                'rows': 10,
                'cols': 80,
            }))
    my_notes = forms.CharField(
        label= '',
        widget=forms.Textarea(
            attrs={
                'class': 'Notes',
                'placeholder': 'Notes:',
                'rows': 10,
                'cols': 80,
            }))            
    speaker = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Speaker:',
            }))
    source = forms.URLField(
        label='',
        widget=forms.URLInput(
            attrs={
                'placeholder': 'Source:',
            }))

    class Meta:
        model = Evidence
        fields = [
            'title',
            'description',
            'speaker',
            'source'
        ]

