from django.urls import path
from .views import listview, createview, updateview, deleteview

app_name = "crud"
urlpatterns = [
    path("", listview, name="list-view"),
    path("create/", createview, name="create-view"),
    path("update/", updateview, name="update-view"),
    path("delete/", deleteview, name="delete-view"),
]
