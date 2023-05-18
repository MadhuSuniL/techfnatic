from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from adminpanel.models import *
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet

class HomeData(ListAPIView):
    
    def get(self,request):
        products = Product.objects.all()
        products = ProductSerializer(products,many=True).data
        # print(products)
        data = {
            'products':products,
            'intro_head':IntroHeading.objects.last().value,
            'intro_sub_head':IntroSubHeading.objects.last().value,
            'about':About.objects.last().value,
            'address':Address.objects.last().value,
            'email':Email.objects.last().value,
            }
        return Response(data)
        

class UpdateData(APIView):
    
    def put(self,request):
        intro_head = request.data.get('intro_head',None)
        intro_sub_head = request.data.get('intro_sub_head')
        email = request.data.get('email')
        about = request.data.get('about')
        address = request.data.get('address')
        
        IntroHeading.objects.create(value=intro_head)
        IntroSubHeading.objects.create(value=intro_sub_head)
        About.objects.create(value=about)
        Email.objects.create(value=email)
        Address.objects.create(value=address)
        
        return Response(None,200)
    
    
class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    
    
        
        