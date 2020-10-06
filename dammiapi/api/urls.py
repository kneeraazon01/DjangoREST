from django.urls import path
from . import views

urlpatterns = [path("", views.apiOverview, name="home"), path("apis/", views.Apis)]
