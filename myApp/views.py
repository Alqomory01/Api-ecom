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
# class Allcarts(APIView):
#     def get_object(self):
#         try:
#             return CartItem.objects.get()
#         except CartItem.DoesNotExist:
#             raise Http404
#     def get(self, request):
#         cartitem = self.get_object()
#         serializer = CartSerializer(cartitem) 
#         return Response(serializer.data)
class Products(APIView):
    def get(self, request):
        obj = Product.objects.all()
        serializers = ProductSerilizer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializers = ProductSerilizer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(APIView):
    def get(self, request):
        
        category= Categorie.objects.all()
        serializer = CategorySerializer(category, many=True)     
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)
       
class BrandListView(APIView): 
    def get(self, request):
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request,  format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class ProductListView(APIView):
#     def get_by_id(self, id):
#         try:
#             obj = Product.objects.get(id=id)
#             return obj
#         except:
#             raise Http404
        
#     def get(self, request, id: str):
#         product = self.get_by_id(id)
#         serializer = ProductSerilizer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, id, format=None):
#         product = self.get_object(id)
#         serializer = ProductSerilizer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_by_id(self, id):
        try:
            obj = Product.objects.get(id=id)
            return obj  # Return the object to use in the get method
        except Product.DoesNotExist:
            raise Http404('product not found')
        
    def get(self, request, id: str, ):
        product = self.get_by_id(id) 
        serializer = ProductSerilizer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, format=None):
        product = self.get_by_id(id)
        serializer = ProductSerilizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id:str):
        product = self.get_by_id(id)
        product.delete()
        return Response({"details:" "product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class ProductCount(APIView):

    def get(self, request):
        count = Product.objects.all().count()
        return Response({"count": count}, status=status.HTTP_200_OK)
    
class ProductByCategory(APIView):
       def get(self, request, category_id:str):
        try:
            # Log the incoming category_id
            print(f"Received category_id: {category_id}")
            # Retrieve the category based on the provided ID
            category = Categorie.objects.get(id=category_id)  # Adjust to match your Category model
            # Now filter products by this category
            products = Product.objects.filter(category=category)
            serializer = ProductSerilizer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categorie.DoesNotExist:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductBrand(APIView):
        def get(self, request, brand_id:int):
            products = Product.objects.filter(brand=brand_id)
            serializer = ProductSerilizer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class ProductSearch(APIView):
        def get(self, request):
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
