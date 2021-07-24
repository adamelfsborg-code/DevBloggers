from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.views import View
from rest_framework.views import APIView
from django.template.loader import get_template
from authentication import authentication as auth
import json
from home import home

class HomeView(View):
    def get(self, request,*args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        page_name = 'Home'

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                email = token[i]['email']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']
                
            return render(request, 'home/home.html', {'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email, 'page_name': page_name})
        return redirect('auth/')

class GetTrendingCategories(APIView):
    def get(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        h = home.Home()
        trending = h.get_trending_categories()

        if len(trending) > 0:
            return Response({'msg': '200', 'items': trending}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND)
        

