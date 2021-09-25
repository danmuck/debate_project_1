from django import forms 

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'title'
            }))
    description = forms.CharField(
            label= '',
        widget=forms.Textarea(
            attrs={
                'class': 'new class name',
                'placeholder': 'description',
                'rows': '5',
                'cols': 80
            }))
    price = forms.DecimalField(
            label= '',
            initial= '19.99',
    )
    email = forms.EmailField(
            label= '',
            required=False,
            
            # initial= '@corning-cc.edu',
            widget=forms.TextInput(
                attrs={
                    'placeholder': '@school-email.edu',
                    'default': 'n/a'
                }
            )

    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not '' in title:
            raise forms.ValidationError('not good title')   
        return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('edu'):
    #         raise forms.ValidationError('not valid email')
    #     return email


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'title'
            }
        )
    )
    description = forms.CharField(
            label= '',
        widget=forms.Textarea(
            attrs={
                'class': 'new class name',
                'placeholder': 'description',
                'rows': '5',
                'cols': 80
            }))
    price = forms.DecimalField(
            label= '',
            initial= '19.99',
    )