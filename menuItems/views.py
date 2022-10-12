from django.shortcuts import render
from rest_framework import generics

from .models import MenuItem
from .serializers import MenuItemSerializer


# Create your views here.


class MenuItemListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
