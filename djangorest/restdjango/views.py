from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import artileSerializer


@api_view(["GET", "POST"])
def articleList(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = artileSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = artileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def articleDetail(request, pk):
    """
    Retrieve, update or delete article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = artileSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = artileSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
