from .models import Comment
from django.forms import ModelForm


class CommentForm(ModelForm):

    def commentauthor(self):
        self.form.instance.author = self.request.user

    class Meta:
        model = Comment
        fields = ['text']

