from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

from django.http import HttpResponse
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  


class TestHelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, Wrold!'}
        return Response(content)

class TestHelloView2(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, Wrold!2auth'}
        return Response(content)



# Create your views here.
def login(request):
    return render(request, 'login.html')

def api_login(request):
    user_name = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = User.objects.create_user(user_name,email,password)
    user.save()
    token = Token.objects.create(user=user)
    print(token.key)
    return HttpResponse("I am from api login")

