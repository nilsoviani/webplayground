from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingrese el título de la publicación'}),
            
            'content': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Ingrese el contenido de la publicación'}),
            
            'order': forms.NumberInput(attrs={
                'class':'form-control', 'placeholder':
                'Ingrese el orden de la publicación'}),
        }
