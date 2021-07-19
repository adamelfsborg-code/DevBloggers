from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfile.as_view(), name='user-profile'),
    path('add-article/', views.AddArticle.as_view(), name='addarticle'),
    path('add-category/', views.AddCategory.as_view(), name='addcategory'),
    path('inbox/', views.Inbox.as_view(), name='inbox'),
    path('statistics/', views.Statistics.as_view(), name='statistics'),
    path('collection/', views.Collection.as_view(), name='collection'),
    path('edit-profile/', views.EditProfile.as_view(), name='editprofile'),
    path('settings/', views.Settings.as_view(), name='settings'),
    path('logout-user/', views.LogoutUser.as_view(), name='logoutuser'),
    path('upload-article/', views.UploadArticle.as_view(), name='uploadarticle'),
    path('create-category/', views.CreateCategory.as_view(), name='createcategory'),
    path('get-user-categories/', views.GetUserCategories.as_view(), name='getusercategories'),
    # path('get-user-articles/', views.GetUserArticles.as_view(), name='getuserarticles'),
    path(r'get-user-articles/', views.GetUserArticles.as_view(), name='getuserarticles')
]
