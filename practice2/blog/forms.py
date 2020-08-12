from django import forms
from .models import Comment, ReComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = '댓글'
        self.fields['body'].widget.attrs.update(
            {'class': 'blog_body', 'placeholder': 'ㅗ'})


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('body', 'comment')
