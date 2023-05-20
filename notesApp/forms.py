from django import forms
from .models import Note


class addForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'categorie']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'body': forms.Textarea(attrs={'class': 'input'}),
            'categorie': forms.Select(attrs={'class': 'input'})
        }