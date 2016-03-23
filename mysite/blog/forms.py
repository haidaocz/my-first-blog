from django import forms
from .models import Post, Comment, Article

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content', 'source_link', )