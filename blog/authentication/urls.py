from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthenticationView.as_view(), name='authentication'),
    path('post-user/', views.PostUser.as_view(), name='postuser'),
    path('login-user/', views.LoginUser.as_view(), name='loginuser'),
    path('check-if-email-exists/', views.CheckIfEmailExists.as_view(), name='checkifemailexists'),
    path('check-if-username-exists/', views.CheckIfUsernameExists.as_view(), name='checkifusernameexists'),
    path('validate-password/', views.ValidatePassword.as_view(), name='validatepassword'),
    path('check-correct-password/', views.CheckCorrectPassword.as_view(), name='checkcorrectpassword')
]
