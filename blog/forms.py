from django import forms
from .models import Comment, Post , Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm h-32 resize-none focus:ring-2 focus:ring-indigo-500 focus:outline-none',
                'placeholder': 'Write a comment'
            }),
        }


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None, 
        widget=forms.Select(attrs={
            'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm bg-white focus:ring-2 focus:ring-indigo-500 focus:outline-none'
        })
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none',
                'placeholder': 'Post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm h-40 resize-none focus:ring-2 focus:ring-indigo-500 focus:outline-none',
                'placeholder': 'Write your post here...'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm bg-white focus:ring-2 focus:ring-indigo-500 focus:outline-none'
            }),
            'image': forms.URLInput(attrs={
                'class': 'w-full rounded-lg border border-slate-300 px-3 py-2 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none',
                'placeholder': 'Image URL (optional)'
            }),
        }