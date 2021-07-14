from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.views import View
from rest_framework.views import APIView
from . import authentication as auth
from django.template.loader import get_template
import json
from base import validate

class AuthenticationView(View):
    def get(self, request, *args, **kwargs):
        
        showmessagemodal = get_template('base/show-messge-modal.html').render()

        return render(request, 'authentication/auth.html',{'showmessagemodal': showmessagemodal})
        

class PostUser(APIView):
    def post(self, request):
        kwargs = {
            'id': request.data.get('id',''),
            'full_name': request.data.get('full_name', ''),
            'username': request.data.get('username', ''),
            'is_blogger': request.data.get('is_blogger', ''),
            'email': request.data.get('email', ''),
            'password': request.data.get('password', '')
        }
        u = auth.User()
        user = u.createUser(**kwargs)
        if 'no results to fetch' in user:
            if not self.request.session.exists(self.request.session.session_key):
                self.request.session.create()
            return Response('Account Created', status=status.HTTP_200_OK)
        return Response('Could not create account', status=status.HTTP_400_BAD_REQUEST)
    

class LoginUser(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        kwargs = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'token': self.request.session.session_key
        }

        u = auth.User()
        user = u.loginUser(**kwargs)

        if user != '404':
            return Response('Logged in', status=status.HTTP_200_OK)
        return Response('Email or password is incorrect') 

class LogoutUser(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return render(request, 'authentication/auth.html')
        
        userid = request.data.get('id')

        u = auth.User()
        user = u.logoutUser(userid)
        
        if 'no results to fetch' in user:
            self.request.session.delete()

            return Response('Logged out',status=status.HTTP_200_OK)
        return Response('Could not logout', status=status.HTTP_400_BAD_REQUEST) 

class CheckIfUsernameExists(APIView):
    def post(self, request):

        username = request.data.get('username')

        u = auth.User()
        user = u.checkIfUsernameExists(username)

        if len(user) > 0:
            return Response('Username does already exists')
        return Response('',status=status.HTTP_200_OK) 

class CheckIfEmailExists(APIView):
    def post(self, request):

        email = request.data.get('email')

        u = auth.User()
        user = u.checkIfEmailExists(email)

        if len(user) > 0:
            return Response('Email does already exists')
        return Response('',status=status.HTTP_200_OK) 

class ValidatePassword(APIView):
    def post(self, request):
        password = request.data.get('password')
        v = validate.password_check(password)
        return Response(v)

