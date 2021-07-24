from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('get-trending-categories/', views.GetTrendingCategories.as_view(), name='gettrendingcategories'),
    path('get-trending-articles/', views.GetTrendingArticles.as_view(), name='gettrendingarticles'),
    path('get-last-visits/', views.GetLastVisits.as_view(), name='getlastvisits')
]