from django.urls import path

from drf import views

urlpatterns = [
    path('api/', views.api),
    path('api/get', views.api_get),
    path('', views.props, name='props')
]
