import django_filters
from .models import Question

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = {
            'title': ['icontains'],  # Case-insensitive title search
            'body': ['icontains'],   # Case-insensitive body search
        }