from datetime import datetime
import random
import re

import requests
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from drf import models, serializers


# Create your views here.

def generate_random_dictionary(num_entries, key_length, value_length):
    random_dict = {}
    for _ in range(num_entries):
        key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=key_length))
        value = ''.join(random.choices('0123456789', k=value_length))
        random_dict[key] = value
    return random_dict

#  {"full_name": "dias", "email": "uaudias@gmail.com", "suggestion": "test"}
# def api(request: HttpRequest) -> JsonResponse:
#     return JsonResponse(data=generate_random_dictionary(100, 5, 10))


# def api_get(request) -> JsonResponse:
#     response = requests.get("http://127.0.0.1:8000/api").json()
#     return JsonResponse(data=response, safe=True)


@api_view(http_method_names=["GET", "POST"])
def props(request: Request) -> Response:
    if request.method == "GET":
        data = serializers.ProposeModelSerializer(models.ProposeModel.objects.all(), many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        full_name = str(request.data.get('FIO'))
        email = str(request.data.get('email', ''))
        suggestion = str(request.data.get('suggestion'))
        date_timestamp = request.data.get('date')
        date_format = datetime.fromtimestamp(date_timestamp / 1000)
        formatted_date = date_format.strftime('%Y-%m-%d %H:%M:%S')
        try:
            validate_email(email)
        except ValidationError:
            return Response(data={"message": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)

        if not full_name or not email or not suggestion:
            return Response(data={"message": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        models.ProposeModel.objects.create(full_name=full_name, email=email, suggestion=suggestion, date=formatted_date)
        return Response(data={"message": "created"}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "DELETE", "PUT", "PATCH"])
def props_del_upd(request: Request, pk) -> Response:
    data = get_object_or_404(models.ProposeModel, id=int(pk))
    if request.method == "GET":
        data = serializers.ProposeModelSerializer(data, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        try:
            data.delete()
            return Response(data={"message": "delete successful"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(data={"error": e}, status=status.HTTP_403_FORBIDDEN)
    elif request.method == "PUT" or request.method == "PATCH":
        full_name = str(request.data.get('full_name', data.full_name))
        email = str(request.data.get('email', data.email))
        suggestion = str(request.data.get('suggestion', data.suggestion))

        try:
            validate_email(email)
        except ValidationError:
            return Response(data={"message": "Invalid email"}, status=status.HTTP_400_BAD_REQUEST)

        if not full_name or not email or not suggestion:
            return Response(data={"message": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        data.full_name = full_name
        data.email = email
        data.suggestion = suggestion

        try:
            data.save()
            return Response(data={"message": "Update successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(http_method_names=["GET", "POST"])
def news(request: Request) -> Response:
    if request.method == "GET":
        news = serializers.NewsModelSerializerMany(models.News.objects.all(), many=True).data
        return Response(data=news, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # Получаем данные из запроса
        category_names = request.data.get('category', [])
        title = request.data.get('title', '')
        description = request.data.get('description', '')

        # Проверяем наличие категорий, заголовка и описания
        if not category_names or not title or not description:
            return Response(data={"message": "Category, title, and description are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Создаем новые категории, если они не существуют
        categories = []
        for category_name in category_names:
            category, created = models.Category.objects.get_or_create(name=category_name)
            categories.append(category)

        # Создаем новость и связываем с категориями
        news = models.News.objects.create(title=title, description=description)
        news.category.set(categories)

        return Response(data={"message": "News created successfully"}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "DELETE"])
def news_one(request: Request, pk: str) -> Response:
    if request.method == "GET":
        new = serializers.NewsModelSerializerOne(models.News.objects.get(id=int(pk)), many=False).data
        return Response(data=new, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        models.News.objects.get(id=int(pk)).delete()
        return Response(data={"message": "Successfully deleted!"}, status=status.HTTP_200_OK)
    else:
        return Response(data={"message": "Method not allowed!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


