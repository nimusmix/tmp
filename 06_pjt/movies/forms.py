from django import forms

from .models import Comment, Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title',
        }),
    )

    score = forms.FloatField(
        widget = forms.NumberInput(attrs={
            'min': '0',
            'max': '5',
            'step': '0.5',
            'class': 'form-control',
            'placeholder': 'Score',
        }),
    )

    description = forms.CharField(
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description',
        })
    )

    class Meta:
        model = Movie
        exclude = ('user',)
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Comment',
        })
    )
    
    class Meta:
        model = Comment
        exclude = ('user', 'movie',)