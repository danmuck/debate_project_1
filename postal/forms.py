from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label= '',
        widget= forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': 'subject',                
            }
        )
    )
    subject = forms.CharField(
        label='',
        required=False,
        widget= forms.TextInput(
            attrs={
                'class': 'subject',
                'placeholder': 'subject',
                
            }
        )
    )

    blogpost = forms.CharField(
        label='',
        widget= forms.Textarea(
            attrs={
                'class': 'blogpost',
                'placeholder': 'blog-post:',
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

