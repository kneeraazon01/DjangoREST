from django.urls import path

from .views import ArticleAPIView, ArticleDetails
from .views import GenericAPIView

urlpatterns = [
    path("generic/article/<int:id>/", GenericAPIView.as_view()),
    path("article/", ArticleAPIView.as_view()),
    path("detail/<int:pk>/", ArticleDetails.as_view()),
]

