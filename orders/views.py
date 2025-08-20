from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
# Create your views here.


class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {'name': 'Margherita Pizza', 'description':'Classic cheese and tomato pizza','price':299},
            {'name': 'Paneer Butter Masala','description':'Paneer cooked in creamy tomato gravy','price': 349},
            {'name':'Veg Biryani','description':'Aromatic rice with mixed vegetsbles','price':249},
            {'name':'Chocolate Brownie','description':'Rich chocolate dessert','price':199},
        ]

        return Response(menu)
