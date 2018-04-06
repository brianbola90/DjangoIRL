from .models import Comment, Post
from django import forms
from taggit_selectize import widgets as tag_widget


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'tags', 'publish']
        widgets = {'title': forms.TextInput(attrs={'class': 'col-md-5 form-control', 'placeholder': 'Title'}),
                   'text': forms.Textarea(),
                   'tags': tag_widget.TagSelectize(attrs={'class': 'col-md-5', 'placeholder': 'Tags'}),
                   'publish': forms.CheckboxInput(attrs={'label': 'publish'})}
