from django.urls import path,include

urlpatterns = [
    path('', include('home.urls')),
    path('auth/', include('authentication.urls')),
    path('profile/', include('userProfile.urls')),
]
