from django.urls import path
from .views import listview, createview, updateview, deleteview

app_name = "crud"
urlpatterns = [
    path("", listview, name="list-view"),
    path("create/", createview, name="create-view"),
    path("update/<int:pk>/", updateview, name="update-view"),
    path("delete/<int:pk>/", deleteview, name="delete-view"),
]
