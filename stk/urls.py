from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('questions/', views.QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('questions/<int:pk>/upvote/', views.QuestionUpvoteView.as_view(), name='question-upvote'),
    path('questions/<int:pk>/downvote/', views.QuestionDownvoteView.as_view(), name='question-downvote'),
    path('questions/<int:pk>/comments/', views.QuestionCommentView.as_view(), name='question-comments'),
]
