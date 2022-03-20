from django.urls import path
from . import views

app_name = "LineBot"
urlpatterns = [
    path('callback', views.callback),
]
