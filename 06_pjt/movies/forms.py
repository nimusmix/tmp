from django import forms

from .models import Comment, Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title',
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
    
    class Meta:
        model = Comment
        exclude = ('user', 'movie',)