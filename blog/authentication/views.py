from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.views import View
from rest_framework.views import APIView
from . import authentication as auth
import json
# Create your views here.
class AuthenticationView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return render(request, 'authentication/auth.html')
        return redirect('/')

class PostUser(APIView):
    def post(self, request):
        kwargs = {
            'id': request.data.get('id',''),
            'full_name': request.data.get('full_name', ''),
            'username': request.data.get('username', ''),
            'profile_image': request.data.get('profile_image', ''),
            'is_blogger': request.data.get('is_blogger', ''),
            'email': request.data.get('email', ''),
            'password': request.data.get('password', '')
        }
        print(kwargs)

        u = auth.User()
        user = u.createUser(**kwargs)
        if 'no results to fetch' in user:
            if not self.request.session.exists(self.request.session.session_key):
                self.request.session.create()
            return Response('Account Created', status=status.HTTP_200_OK)
        return Response('Could not create account', status=status.HTTP_400_BAD_REQUEST)
    

class LoginUser(APIView):
    def post(self, request):
        kwargs = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'token': self.request.session.session_key
        }

        u = auth.User()
        user = u.loginUser(**kwargs)
        if 'no results to fetch' in user:
            return Response('Logged In', status=status.HTTP_200_OK)
        return Response('Could Not Login', status=status.HTTP_400_BAD_REQUEST)

