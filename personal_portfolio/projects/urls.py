import os
from django.urls import path
from . import views


# DEfine urlpatterns
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
