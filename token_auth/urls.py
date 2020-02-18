
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token
from token_app.views import api_login
from token_app.views import login
from token_app.views import rest_model_json


#another 

from token_app import views as appviews





urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api_login/', api_login),
    path('hello/', appviews.TestHelloView.as_view()),
    path('hello2/', appviews.TestHelloView2.as_view()),
    path('rest_model_json/',rest_model_json),

]
