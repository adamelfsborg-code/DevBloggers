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

class SearchView(View):
    def get(self, request,*args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        page_name = 'Search'

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
                
            return render(request, 'home/search.html', {'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email, 'page_name': page_name})
        return redirect('auth/')

class LatestArticlesView(View):
    def get(self, request,*args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        page_name = 'Latest articles'

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
                
            return render(request, 'home/latest-articles.html', {'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email, 'page_name': page_name})
        return redirect('auth/')

class ArticlesView(View):
    def get(self, request, *args,**kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        page_name = 'Articles'

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

            return render(request, 'home/articles.html', {'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email, 'page_name': page_name})
        return redirect('auth/')

class GetArticlesByCategory(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
            
        

        kwargs = {
            'category_name': request.data.get('category'),
            'limit': request.data.get('limit'),
            'offset': request.data.get('offset')
        }

        h = home.Home()
        articles = h.articles(**kwargs)
        if len(articles) > 0:
            return Response({'msg': '200', 'items': articles}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND) 

class GetCategoryByName(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
            
        
        category_name =  request.data.get('category')
        
        h = home.Home()
        category = h.category(category_name)

        if len(category) > 0:
            return Response({'msg': '200', 'items': category}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND)   

class GetArticlesCount(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
            
        
        category_name =  request.data.get('category')
        
        h = home.Home()
        articles = h.get_articles_count(category_name)

        if len(articles) > 0:
            return Response({'msg': '200', 'items': articles}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND)   


class GetTrendingCategories(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        date = request.data.get('date')

        h = home.Home()
        trending = h.get_trending_categories(date)

        if len(trending) > 0:
            return Response({'msg': '200', 'items': trending}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND)
        
class GetTrendingArticles(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        date = request.data.get('date')

        h = home.Home()
        trending = h.get_trending_articles(date)

        if len(trending) > 0:
            return Response({'msg': '200', 'items': trending}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND) 

class GetLastVisits(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
        
        kwargs = {
            'date': request.data.get('date'),
            'user_id': request.data.get('user_id')
        }

        h = home.Home()
        visit = h.get_last_visits(**kwargs)

        if len(visit) > 0:
            return Response({'msg': '200', 'items': visit}, status=status.HTTP_200_OK)
        return Response({'msg': '404'}, status=status.HTTP_404_NOT_FOUND) 

class GetBloggers(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        param = request.data.get('param')

        h = home.Home()
        search = h.get_bloggers_search(param)

        if len(search) > 0:
            return Response({'msg': '200', 'items': search}, status=status.HTTP_200_OK)
        return Response({'msg': 'no items'}, status=status.HTTP_200_OK)

class GetCategories(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
        
        param = request.data.get('param')
        h = home.Home()
        search = h.get_categories_search(param)

        if len(search) > 0:
            return Response({'msg': '200', 'items': search}, status=status.HTTP_200_OK)
        return Response({'msg': 'no items'}, status=status.HTTP_200_OK)

class GetArticles(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
        
        param = request.data.get('param')
        h = home.Home()
        search = h.get_articles_search(param)

        if len(search) > 0:
            return Response({'msg': '200', 'items': search}, status=status.HTTP_200_OK)
        return Response({'msg': 'no items'}, status=status.HTTP_200_OK)

class GetLatestArticles(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')
        
        kwargs = {
            'followers_only':request.data.get('followersOnly') ,
            'user_id': request.data.get('user_id')
        }
        
        h = home.Home()
        search = h.get_latest_articles(**kwargs)

        if len(search) > 0:
            return Response({'msg': '200', 'items': search}, status=status.HTTP_200_OK)
        return Response({'msg': 'no items'}, status=status.HTTP_200_OK)