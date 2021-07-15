from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from authentication import authentication as auth
from django.views import View
from rest_framework.views import APIView
from django.template.loader import get_template
import json
# Create your views here.

class UserProfile(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        if is_blogger:
            page_name = 'Your Blog'
            return render(request, 'userProfile/pages/blog-profile.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })
        
        page_name = 'Inbox'
        return render(request, 'userProfile/pages/inbox.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })
        
class Inbox(APIView):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Inbox' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/inbox.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            
class Statistics(APIView):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Statistics' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/statistics.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            
class Collection(APIView):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Collection' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/statistics.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })

class EditProfile(APIView):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Edit Profile' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/statistics.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            
class Settings(APIView):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Settings' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/statistics.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            


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