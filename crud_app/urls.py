from django.urls import path
from .views import listview, createview, updateview, deleteview

urlpatterns = [
    path("", listview, name="list-view"),
    path("crate/", createview, name="crete-view"),
    path("update/", updateview, name="update-view"),
    path("delete/", deleteview, name="delete-view"),
]
