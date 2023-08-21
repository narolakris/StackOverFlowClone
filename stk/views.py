from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import QuestionSerializer
from .filters import QuestionFilter

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,) 

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Question
from .serializers import QuestionSerializer

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuestionFilter
    ordering_fields = ['title', 'vote_count']  
    permission_classes = (IsAuthenticatedOrReadOnly,)

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)

from .models import Vote
from .serializers import VoteSerializer

class QuestionUpvoteView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, vote_type='upvote', question_id=self.kwargs['pk'])

class QuestionDownvoteView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, vote_type='downvote', question_id=self.kwargs['pk'])

from .models import Comment
from .serializers import CommentSerializer

class QuestionCommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        question_id = self.kwargs['pk']
        return Comment.objects.filter(question_id=question_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, question_id=self.kwargs['pk'])