from django.urls import path
from .views import articleList, articleDetail

urlpatterns = [path("article/", articleList), path("detail/<int:pk>/", articleDetail)]
