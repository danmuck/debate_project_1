from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label= '',
        widget= forms.TextInput(
            attrs={
                
            }
        )
    )
    subject = forms.CharField(
        label='',
        required=False,
        widget= forms.TextInput(
            attrs={
                
            }
        )
    )

    blogpost = forms.CharField(
        label='',
        widget= forms.Textarea(
            attrs={
                'class': 'blogpost',
                'rows': 10,
                'cols': 100,
            }
        )
    )
    
    class Meta:
        model = Article
        fields = (
            "title",
            'subject',
            'blogpost',
        )

