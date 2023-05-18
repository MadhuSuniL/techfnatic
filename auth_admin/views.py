from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
import random
import string
from .email_send import EmailThread
from django.conf import settings


def generate_password(length=random.randint(8, 15)):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password




class Registration(APIView):
    
    def get(self,request):
        user = request.user
        type_admin = 'Admin'
        if user.is_staff and user.is_superuser:
            type_admin = 'SuperAdmin'
        data = {
            'username':user.username,
            'type':type_admin
        }
        print(data)
            
        return Response(data,200)

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        
        try:
            user = User.objects.create_user(username=username,password=password,is_staff=True)
            refresh_token = RefreshToken.for_user(user)

            data = {
                'refresh':str(refresh_token),
                'access':str(refresh_token.access_token)
            }
            return Response(data,200)
        except:
            return Response('Admin already exist!',400)

class Login(APIView):
    
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            type_admin = 'Admin'
            if user.is_staff and user.is_superuser:
                type_admin = 'SuperAdmin'
        
            refresh_token = RefreshToken.for_user(user)
            data = {
                'refresh':str(refresh_token),
                'access':str(refresh_token.access_token),
                'username':user.username,
                'admin_type': type_admin
                
            }
            return Response(data,200)
        return Response('Admin Not Found!',404)
         
        
class AdminList(APIView):
    
    def get(slef,request):
        admins = User.objects.filter(is_staff=True , is_superuser=False)
        data = UserSerializer(admins,many=True).data
        return Response(data)
    
    
class SendInvitation(APIView):
    
    def post(self,request):
        # try:
            user_email = request.data['email']
            names = ['Name1','Name2','Name3','Name4']
            random_username = random.choice(names)
            random_password = generate_password()
            user = User.objects.create_user(username=random_username,password=random_password,is_staff=True)

            
            
            html = f"""
            <h1 style='color:green;font-size:50px'>Admin invitation from <b>TechFnatic</b> </h1>

                <h3>Username : <b>{random_username}</b></h3>
                <h3>Password : <b>{random_password}</b></h3>
            """
            
            
            email_ = EmailThread('Admin Invitation', html, settings.EMAIL_HOST_USER, [user_email])
            email_.start()
            return Response(None,200)
        # except:
        #     return Response(None,400)
        