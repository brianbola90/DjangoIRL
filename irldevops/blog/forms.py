from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'publish']
        widgets = {'title': forms.TextInput(attrs={'class': 'col-md-5 form-control', 'placeholder': 'Title'}),
                   'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Post content'}),
                   'publish': forms.CheckboxInput(attrs={'label': 'publish'})}
