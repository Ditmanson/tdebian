
from django.urls import path

from . import views

urlpatterns = [
    path("", views.techIndex, name="techIndex"),
    path("content/", views.techContent, name="techContent"),
    path("<str:myTag>/", views.techTag, name="techTag"),
]
