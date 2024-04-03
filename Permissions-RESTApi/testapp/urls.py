from django.urls import path
from .views import *
urlpatterns = [
    path('', ListCreateUsers.as_view(), name="users"),
]