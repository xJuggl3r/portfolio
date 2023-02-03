# import forms
from django import forms
from .models import Post, Comment

# Create the form class.


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'header_image',
                  'image1', 'image2', 'categories',)


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
