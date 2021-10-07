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
                'required': False,
            })) 
    # opposed = forms.CharField(
    #     label= 'opposition:',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'opposed',
    #             'placeholder': 'Opposition:',
    #             'rows': 10,
    #             'cols': 80,
    #             'required': False,
    #         }))                        
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
                'required': False,
                'placeholder': 'Source:',
            }))

    class Meta:
        model = Evidence
        fields = [
            'title',
            'description',
            'my_notes',
            # 'opposed'
            'speaker',
            'source'
        ]

