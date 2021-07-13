from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthenticationView.as_view(), name='authentication'),
    path('post-user/', views.PostUser.as_view(), name='postuser'),
    path('login-user/', views.LoginUser.as_view(), name='loginuser'),
]
