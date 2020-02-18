from django.shortcuts import render
from django.contrib.auth.models import User
from token_app.models import RestModel
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


#model data to json
from django.core import serializers

from django.http import HttpResponse
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated  
from django.views.decorators.csrf import csrf_exempt


class TestHelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, Wrold!'}
        return Response(content)

class TestHelloView2(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, Wrold!2auth this is authenticated '}
        return Response(content)

def rest_model_json(request):
    #all_data = RestModel.objects.all();
    all_data = RestModel.objects.order_by('data3');
    data_list = serializers.serialize('json', all_data)
    return HttpResponse(data_list, content_type="text/json-comment-filtered")




# Create your views here.
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def api_login(request):
    user_name = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = User.objects.create_user(user_name,email,password)
    user.save()
    token = Token.objects.create(user=user)
    print(token.key)
    return HttpResponse("I am from api login")

