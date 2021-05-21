from django.urls import path
from . import views

urlpatterns = [
    path('getAuthorize', views.getAuthorize),
    path('apiNotify', views.apiNotify),
]
