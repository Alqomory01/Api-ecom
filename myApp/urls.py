from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', Allcarts.as_view(), name='cart'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>/', ProductListView.as_view(), name='productlist'),
    path('brand/<int:pk>/', BrandListView.as_view(), name='brand'),
    
]