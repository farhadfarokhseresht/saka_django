from django.urls import path
from saka import views

app_name = "saka"
urlpatterns = [
    path('', views.index, name='index'),
    path("signin", views.signin,name='signin'),
    path("labpage", views.labpage,name='labpage'),
    path("formB", views.formB,name='formB'),
    path("report", views.report,name='report'),
    path("test", views.test,name='test'),
    path("log_out", views.log_out,name='log_out'),
]
