# listings/urls.py

from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def index(request):
    return Response({"message": "Welcome to the Listings API!"})


urlpatterns = [
    path('', index),
]
