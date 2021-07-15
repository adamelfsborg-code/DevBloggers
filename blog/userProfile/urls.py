from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfile.as_view(), name='user-profile'),
    path('logout-user/', views.LogoutUser.as_view(), name='logoutuser'),
    path('inbox/', views.Inbox.as_view(), name='inbox'),
    path('statistics/', views.Statistics.as_view(), name='statistics'),
    path('collection/', views.Collection.as_view(), name='collection'),
    path('edit-profile/', views.EditProfile.as_view(), name='editprofile'),
    path('settings/', views.Settings.as_view(), name='settings')
]
