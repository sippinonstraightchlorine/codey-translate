from django.urls import path
from . import views

urlpatterns = [
    path("", views.ceviri_view, name="ceviri"),
]
