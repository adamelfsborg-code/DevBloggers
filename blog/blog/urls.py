from django.urls import path,include

urlpatterns = [
    path('', include('base.urls')),
    path('auth/', include('authentication.urls')),
]
