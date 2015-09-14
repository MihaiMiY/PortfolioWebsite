from django import forms
from blog.models import Post
from models import Settings

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text', 'category')

class SettingsForm(forms.ModelForm):

	class Meta:
		model = Settings
		fields = ('title', 'slug', 'description')

