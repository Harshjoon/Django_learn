from django.contrib import admin
from django.urls    import path

from .              import views

urlpatterns = [
    path("mainpage/", views.main_page, name="form-main"),
    path("about/", views.about_page, name="form-about"),
    path("forms/", views.forms_page, name="form-form"),
    path("editforms/", views.edit_page, name="form-edit"),
    path("", views.home_page, name="form-home"),
]