from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'user', 'vote_count')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'user', 'question', 'vote_type')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'question')