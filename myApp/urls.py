from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', Allcarts.as_view(), name='cart'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>/', ProductListView.as_view(), name='productlist'),
    path('brand/<int:pk>/', BrandListView.as_view(), name='brand'),
    path('<str:query>/', ProductSearch.as_view(), name='productsearch'),
    path('<str:pk>/', ProductDetail.as_view, name='productdetail'),
    path('sort/category/<int:pk>/', ProductByCategory.as_view(), name='category'),
    path('sort/brand/<int:pk>/', ProductBrand.as_view(), name='brand'),
    path('sount/', ProductCount.as_view(), name='productcount')
    
]