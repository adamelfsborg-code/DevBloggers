from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base-view'),
]
