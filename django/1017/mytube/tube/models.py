from django.db import models
from django.contrib.auth.models import User

class TubePost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    video = models.FileField(upload_to='tube/videos/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(
        TubePost, on_delete=models.CASCADE, related_name='comments'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.message
