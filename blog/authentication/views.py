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

        page_name = 'Authentication'

        return render(request, 'authentication/auth.html',{'showmessagemodal': showmessagemodal, 'page_name': page_name})
        

class PostUser(APIView):
    def post(self, request):
        kwargs = {
            'id': request.data.get('id',''),
            'full_name': request.data.get('full_name', ''),
            'username': request.data.get('username', ''),
            'is_blogger': request.data.get('is_blogger', ''),
            'email': request.data.get('email', ''),
            'password': request.data.get('password', ''),
            'profile_image': request.data.get('profile_image', '')
        }
        u = auth.User()
        user = u.createUser(**kwargs)
        print(user)
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

class CheckIfUsernameExists(APIView):
    def post(self, request):

        username = request.data.get('username')
        print(username)
        u = auth.User()
        user = u.checkIfUsernameExists(username)
        if len(user) > 0:
            print(user)
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
        print(password)
        v = validate.password_check(password)
        print(v)
        return Response(v)


class CheckCorrectPassword(APIView):
    def post(self, request):

        kwargs = {
            'id': request.data.get('id'),
            'password': request.data.get('password')
        }

        u = auth.User()
        user = u.check_correct_password(**kwargs)

        if len(user) > 0:
            return Response('200', status=status.HTTP_200_OK)
        return Response('400',status=status.HTTP_400_BAD_REQUEST) 