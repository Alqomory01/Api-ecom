from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .models import cart , CartItem
from rest_framework.response import Response
from django.http import Http404
from .serializers import *

# create you vies here
class CartViewSet(viewsets.ModelViewSet):

    serializer_class = CreateCartItemSeriazer
    queryset = CartItem





# Create your views here.
