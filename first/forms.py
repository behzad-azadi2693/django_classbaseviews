from django import forms
from .models import Comment

class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=150)


class TodoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('namme', 'body')
        