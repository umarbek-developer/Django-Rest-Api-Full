from django.shortcuts import render
# from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict


from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializer import ProductSerializer 

# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    data = request.data

    instance = Product.objects.all.order_by("?").first() 
    data = {}

    # if instance:
    #     # data = model_to_dict(instance, fields=['id', 
    #     # 'title', 'price', 'sale_price])
    #     data = ProductSerializer(instance).data

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
    return Response(serializer.data)