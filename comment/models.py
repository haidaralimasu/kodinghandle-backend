from datetime import datetime
from blog.models import BlogPost
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment
