from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('latest-articles', views.LatestArticlesView.as_view(), name='latestarticles'),
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    path('get-trending-categories/', views.GetTrendingCategories.as_view(), name='gettrendingcategories'),
    path('get-trending-articles/', views.GetTrendingArticles.as_view(), name='gettrendingarticles'),
    path('get-last-visits/', views.GetLastVisits.as_view(), name='getlastvisits'),
    path('get-bloggers/', views.GetBloggers.as_view(), name='getbloggers'),
    path('get-categories/', views.GetCategories.as_view(), name='getcategories'),
    path('get-articles/', views.GetArticles.as_view(), name='getarticles'),
    path('get-latest-articles/', views.GetLatestArticles.as_view(), name='getlatestarticles'),
    path('get-articles-page/', views.GetArticlesByCategory.as_view(), name='getarticlesbycategory'),
    path('get-category-by-name/', views.GetCategoryByName.as_view(), name='getcategorybyname'),
    path('get-articles-count/', views.GetArticlesCount.as_view(), name='getarticlescount')
]