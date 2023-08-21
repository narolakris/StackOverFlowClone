from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10)

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

