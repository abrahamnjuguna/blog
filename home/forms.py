from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['date']
    title = forms.CharField(label="Title")
    sub_title = forms.CharField(label="Sub Title")
    content = forms.CharField(label="Content",widget=CKEditorUploadingWidget())
    poster = forms.ImageField()
    facebook_link = forms.URLField()
    twitter_link = forms.URLField()
    instagram_link = forms.URLField()
    linkedin_link = forms.URLField()