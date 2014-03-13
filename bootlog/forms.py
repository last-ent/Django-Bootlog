from django import forms

class CommentForm(forms.Form):
	comment = forms.CharField()
	handle = forms.CharField(required=False)
	#post = forms.ForeignKey(Post)