from django.conf.urls import url
from . import views

app_name = "Stock"
urlpatterns = [
    url(r'^stock/$', views.stock, name='stock'),
]
