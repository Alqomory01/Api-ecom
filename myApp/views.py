from django.shortcuts import render
from django.http import Http404
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q



# @api_view(['GET'])
# def all_categories(request):
#     categories = Category.objects.all()
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
class Allcarts(APIView):
    def get_object(self):
        try:
            return CartItem.objects.get()
        except CartItem.DoesNotExist:
            raise Http404
    def get(self, request):
        cartitem = self.get_object()
        serializer = CartSerializer(cartitem) 
        return Response(serializer.data)


class CategoryListView(APIView):
    def get_object(self, pk):
        try:
            return Categorie.objects.get(pk=pk)
        except Categorie.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        category= self.get_object(pk)
        serializer = CategorySerializer(category)     
        return Response(serializer.data)
    
    def put(self, request, format=None):
        category = self.get_object()
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BrandListView(APIView):
    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        brand = self.get_category(request, pk)
        brand.delete()

class ProductListView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerilizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_by_id(id:str):
        try:
            return Product.objects.get(id=id)
        except:
            raise Http404('product not found')
        
    def get(self, request, pk:str, format=None):
        product = self.get_by_id(pk)
        serializer = ProductSerilizer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk:str, format=None):
        product = self.get_by_id(pk)
        serializer = ProductSerilizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk:str):
        product = self.get_by_id(pk)
        product.delete()
        return Response({"details:" "product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class ProductCount(APIView):

    def get(self, request, format=None):
        count = Product.objects.count()
        return Response({"count": count}, status=status.HTTP_200_OK)
    
class ProductByCategory(APIView):
        def get(self, request, category_id:int, format=None):
            products = Product.objects.filter(category_id=category_id)
            serializer = ProductSerilizer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class ProductBrand(APIView):
        def get(self, request, brand_id:int, format=None):
            products = Product.objects.filter(brand_id=brand_id)
            serializer = ProductSerilizer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class ProductSearch(APIView):
        def get(self, request, search_term:str, format=None):
            search_query = request.data.get("query" "")
            if search_query:
                search_results = Product.objects.filter(
                    Q(name_icontains=search_query)
                    | Q(category__icontains=search_query)
                    | Q(brand__icontains=search_query)
                    | Q(price__icontains=search_query)
                )
                search_results = search_results.order_by("id")
                serializer = Product(search_results, many=True)
                return Response(serializer.data)
            return Response("invalid search query", status=status.HTTP_400_BAD_REQUEST)
        
    
# Create your views here.
