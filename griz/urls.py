from django.urls import path

from . import views

urlpatterns = [
    path("", views.grizIndex, name="grizIndex"),
]
