from django.contrib import admin
from django.urls    import path

from .              import views

urlpatterns = [
    path("mainpage/", views.form_page, name="form-form"),
    path("about/", views.about_page, name="form-about"),
    path("", views.home_page, name="form-home"),
]