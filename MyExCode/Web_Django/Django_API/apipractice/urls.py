from django.urls import path
from . import views

urlpatterns = [
    path('addUser', views.addUser),
    path('delUser', views.delUser),
    path('getUserInfo', views.getUserInfo),
]
