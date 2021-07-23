from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.views import View
from rest_framework.views import APIView
from django.template.loader import get_template
import json

class HomeView(APIView):
    def get(self, request,*args, **kwargs):

        page_name = 'Home'

        return render(request, 'home/home.html', {'page_name': page_name})