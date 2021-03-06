from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import *

urlpatterns = [
    path('snippets/', snippetsViews.SnippetList.as_view()),
    path('snippets/<int:pk>/', snippetsViews.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
