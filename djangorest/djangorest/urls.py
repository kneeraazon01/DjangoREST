from django.contrib import admin
from django.urls import path, include
from restdjango.views import ArticleViewSet
from rest_framework.routers import DefaultRouter
 
 
router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
 
 
urlpatterns = [
 
    path('', include(router.urls))
 
 
]