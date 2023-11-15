from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from drf import views

urlpatterns = [
    path("", views.home, name="home"),
    # path('api/get', views.api_get),
    path("api/", views.props),
    path("api/<str:pk>", views.props_del_upd),
    path("api/news/", views.news),
    path("api/news/<str:pk>", views.news_one),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
