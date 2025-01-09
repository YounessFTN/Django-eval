# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']

    content = forms.CharField(widget=forms.Textarea, label="Votre commentaire")
    rating = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], label="Note", widget=forms.RadioSelect)
