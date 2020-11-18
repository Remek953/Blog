from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=50)
	email  = forms.EmailField(required=False, max_length=100)
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

		widgets = {
				'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
				'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
				'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment'}),
		}

		labels = {
		"name": "",
		"email": "",
        "body": "",
    	}
