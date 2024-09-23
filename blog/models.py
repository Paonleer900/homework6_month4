from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=250, null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,)

    def __str__(self):
        return self.title

