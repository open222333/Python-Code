from django.urls import path
from . import views

urlpatterns = [
    path('getLink', views.getLink),
    path('getAuthorize', views.getAuthorize),
    path('apiNotify', views.apiNotify),
]
