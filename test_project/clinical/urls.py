from django.contrib import admin
from django.urls    import path

from .              import views

urlpatterns = [
    path("", views.fill_data, name="clinical-fill_data"),
]

