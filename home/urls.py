from django.urls import path
from .views import *

urlpatterns = [
    path("/notes", note_list, name = "note_List"),
]