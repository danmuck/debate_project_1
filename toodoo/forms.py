from django import forms 

from .models import TooDoo

class TooDooList(forms.ModelForm):
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
                'rows': '22',
                'cols': 80
            }))

    class Meta:
        model = TooDoo
        fields = [
            'title',
            'description',
            # 'date'
        ]

