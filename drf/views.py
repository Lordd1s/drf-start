import datetime
import random
import re

import requests
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from drf import models


# Create your views here.

def generate_random_dictionary(num_entries, key_length, value_length):
    random_dict = {}
    for _ in range(num_entries):
        key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=key_length))
        value = ''.join(random.choices('0123456789', k=value_length))
        random_dict[key] = value
    return random_dict


def api(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data=generate_random_dictionary(100, 5, 10))


def api_get(request) -> JsonResponse:
    response = requests.get("http://127.0.0.1:8000/api").json()
    return JsonResponse(data=response, safe=True)


def props(request):
    if request.method == "GET":
        return render(request, "props.html")
    elif request.method == "POST":
        full_name = request.POST.get("fullName")
        email = request.POST.get("email")
        suggestion = request.POST.get("suggestion")
        date = datetime.datetime.now().strftime("%d.%m.%Y")
        switch = request.POST.get("switch")

        regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        print(request.body)
        if re.match(regex_email, string=email):
            if not full_name or not email or not suggestion:
                return render(request, "props.html", context={"error": "Заполните все поля"})

            if switch is None:
                models.ProposeModel.objects.create(full_name=full_name, email=email, suggestion=suggestion)
            elif switch == 'on':
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO drf_proposemodel (full_name, email, suggestion, date) VALUES (?, ?, ?, ?)", (full_name, email, suggestion, date))

        else:
            return render(request, "props.html", context={"error": "Введите правильный email"})

        return render(request, "props.html", context={"success": "Успешно отправлено"})
