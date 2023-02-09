from django.db import models

# Create your models here.

class Post(models.Model):
    '''Model for forum posts'''
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey("nhl_auth.NHLUser", on_delete=models.CASCADE, related_name="posts", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    '''Model for forum comments'''
    content = models.CharField(max_length=1000)
    author = models.ForeignKey("nhl_auth.NHLUser", on_delete=models.CASCADE, related_name="comments", null=True)
    post = models.ForeignKey("forum.Post", on_delete=models.CASCADE, related_name="comments", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Topic(models.Model):
    '''Model for forum topics'''
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField("forum.Post", related_name="topics", null=True)

