from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    poster = models.ImageField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    linkedin_link = models.URLField()

    def __str__(self):
        return self.title
    

class Message(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return f"{self.first_name} - {self.email}"