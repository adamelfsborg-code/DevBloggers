from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from authentication import authentication as auth
from . import userProfile as uP
from django.views import View
from rest_framework.views import APIView
from django.template.loader import get_template
import json
# Create your views here.

class UserProfile(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        

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

        if is_blogger:
            page_name = 'Your Blog'
            return render(request, 'userProfile/pages/blog-profile.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger, 'email': email, 'showmessagemodal': showmessagemodal, 'page_name': page_name })
        
        page_name = 'Inbox'
        return render(request, 'userProfile/pages/inbox.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })

class AddArticle(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Add Article' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                email = token[i]['email']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/add-article.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })
           
class AddCategory(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Add Category' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                email = token[i]['email']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/add-category.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })
               

class Inbox(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Inbox' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                email = token[i]['email']
                username = token[i]['username']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/inbox.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            
class Statistics(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Statistics' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                email = token[i]['email']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/statistics.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            
class Collection(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Collection' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                email = token[i]['email']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/collection.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })

class EditProfile(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Edit Profile' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                email = token[i]['email']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/edit-profile.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            
class Settings(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()

        page_name = 'Settings' 

        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                email = token[i]['email']
                fullname = token[i]['fullname']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']

        return render(request, 'userProfile/pages/statistics.html',{'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email,'showmessagemodal': showmessagemodal, 'page_name': page_name })
            


class LogoutUser(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')
        
        userid = request.data.get('id')

        u = auth.User()
        user = u.logoutUser(userid)
        
        if 'no results to fetch' in user:
            self.request.session.delete()

            return Response('Logged out',status=status.HTTP_200_OK)
        return Response('Could not logout', status=status.HTTP_400_BAD_REQUEST) 

class UploadArticle(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        blocks = json.dumps(request.data.get('blocks'))

        kwargs = {
            'article_id': request.data.get('article_id', ''),
            'user_id': request.data.get('user_id'),
            'publish_date': request.data.get('publish_date'),
            'category_id': request.data.get('category_id'),
            'blocks': blocks,
        }

        u = uP.Profile()
        profile = u.add_article(**kwargs)

        if len(profile) > 0:
            for i in profile:
                if 'article_updated' not in i:
                    id = i.get('id')
                    return Response({'msg': 'Article Uploaded', 'id': id  },status=status.HTTP_200_OK) 
                return Response({'msg': 'Article Updated'},status=status.HTTP_200_OK) 
            return Response('Artilce Not Uploaded', status=status.HTTP_400_BAD_REQUEST)

class CreateCategory(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        kwargs = {
            'id': request.data.get('id', ''),
            'user_id': request.data.get('user_id'),
            'name': request.data.get('name'),
            'icon': request.data.get('icon'),
            'background_color': request.data.get('background_color'),
            'text_color': request.data.get('text_color'),
        }        

        u = uP.Profile()
        profile = u.add_category(**kwargs)

        if len(profile) > 0:
            for i in profile:
                if 'category_updated' not in i:
                    print(profile)
                    id = i.get('id')
                    return Response({'msg': 'Category Created', 'id': id}, status=status.HTTP_200_OK)
                return Response({'msg': 'Category Updated'},status=status.HTTP_200_OK)
            return Response('Category Not Created', status=status.HTTP_400_BAD_REQUEST)

class GetUserCategories(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')
        
        user_id = request.data.get('user_id')

        u = uP.Profile()
        profile = u.get_user_categories(user_id)

        if len(profile) > 0:
            return Response({'msg': '200', 'items': profile}, status=status.HTTP_200_OK)
        return Response({'msg': 'Categories not found'},status=status.HTTP_200_OK)

class GetUserArticles(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('/auth/')

        user_id = request.data.get('user_id')

        u = uP.Profile()
        profile = u.get_user_articles(user_id)

        if len(profile) > 0:
            return Response({'msg': '200', 'items': profile}, status=status.HTTP_200_OK)
        return Response({'msg': 'Categories not found'},status=status.HTTP_200_OK) 