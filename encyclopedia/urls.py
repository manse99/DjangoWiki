from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # the index page
    path("wiki/<str:title>", views.entry_page, name="entry"), #route for individual entries
]
