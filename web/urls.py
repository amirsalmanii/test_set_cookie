from django.urls import path
from .views import TestView, TestView2

urlpatterns = [
    path("test/", TestView.as_view()),
    path("test2/", TestView2.as_view()),
]