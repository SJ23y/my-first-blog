from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):
	text = forms.CharField(widget=SummernoteWidget())

	class Meta:
		model = Post
		fields = ('title','text', 'image')
    
        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text')


