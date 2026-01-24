from django.urls import path

from . import views

urlpatterns = [
    path("", views.grizIndex, name="grizIndex"),
    path("content/", views.grizContent, name="grizContent"),
    path("<str:myTag>/", views.grizTag, name="grizTag"),
]
