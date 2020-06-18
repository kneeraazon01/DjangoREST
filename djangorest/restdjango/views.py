from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import artileSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def articleList(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = artileSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = artileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
