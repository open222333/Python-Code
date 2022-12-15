from django.urls import path
from django.conf.urls import url
from . import views

# 避免路由硬編碼
app_name = "Login"
urlpatterns = [
    path('', views.index, name="login"),
    url(r'^verify/$', views.googleVerify),
    url(r'^user/$', views.userPage, name="user"),
    url(r'^main/$', views.mainPage, name="main"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^useradd/$', views.useradd, name="useradd"),
    url(r'^useraddforms/$', views.useraddforms, name="useraddforms"),
    url(r'^useredit/$', views.useredit, name="useredit"),
    path('<id>/', views.usereditforms, name="usereditforms"),
    path('.well-known/pki-validation/5E2440DD33F318F86C43B03EA08B6B62.txt',
         views.txtPage),  # 驗證ssl證書用
    # url(r'^testpage/$', views.testPage, name="testpage"),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
