from django.urls import path
from . import views

# URLConf module
urlpatterns = [path("playground/hello", views.say_hello)]
