from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '40', 'rows': '5', 'max_length': '200'}))

    class Meta:
        model = Post
        fields = ("user", "text")
