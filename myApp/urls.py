from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('product/', Products.as_view(), name='products'),
    # path('', Allcarts.as_view(), name='cart'),
    path('categories/', CategoryListView.as_view(), name='category'),
    # path('<str:id>/', ProductListView.as_view(), name='productlist'),
    path('brands/', BrandListView.as_view(), name='brand'),
    path('<str:query>/', ProductSearch.as_view(), name='productsearch'),
    path('<str:id>/', ProductDetail.as_view, name='productdetail'),
    path('sort/category/<int:pk>/', ProductByCategory.as_view(), name='sort-by-category'),
    path('sort/brand/<int:pk>/', ProductBrand.as_view(), name='sort-by-brand'),
    path('count/', ProductCount.as_view(), name='productcount')
    
]