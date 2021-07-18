from django.shortcuts import render,redirect
from django.views import View
from authentication import authentication as auth
from django.template.loader import get_template
import json
# Create your views here.

class BaseView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            return redirect('auth/')

        showmessagemodal = get_template('base/show-messge-modal.html').render()
        
        u = auth.User()
        token = u.getUser(self.request.session.session_key)
        if len(token) > 0:
            for i,a in enumerate(token):
                id = token[i]['id']
                username = token[i]['username']
                fullname = token[i]['fullname']
                email = token[i]['email']
                profile_image = token[i]['profile_image']
                is_blogger = token[i]['is_blogger']
                
            return render(request, 'base/index.html', {'id': id, 'username': username, 'fullname': fullname, 'profile_image': profile_image, 'is_blogger': is_blogger,'email': email, 'showmessagemodal': showmessagemodal })
        return redirect('auth/')
