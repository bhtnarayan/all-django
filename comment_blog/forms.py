from django import forms 
from . models import Post
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Your Name...',
            }
        )
    )
    body = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'rows': 5,
                'class': 'form-control',
                'placeholder': 'Leave a comment',
            }
        )
    )

