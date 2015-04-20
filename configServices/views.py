from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from mongoengine.django.auth import User
from django.contrib import auth
from django.template import RequestContext
from django.core.context_processors import csrf
from config.models import Config

import logging

logger = logging.getLogger(__name__)

def login(request):
   c = {}
   c.update(csrf(request))
   return render_to_response('login.html', c)

def auth_view(request):
   username = request.POST['username']
   password = request.POST['password']
   #user = auth.authenticate(username=username, password=password)
   user = User.objects.get(username=username)
   if user is not None and user.check_password(password):
       user._meta.pk = user._meta['id_field']
       logger.info(user._meta.pk)
       user.backend = 'mongoengine.django.auth.MongoEngineBackend'

       auth.login(request, user)
       request.session.set_expiry(60 * 60 * 1)  # 1 hour timeout
       #params = { 'isloggedin': auth.user_logged_in, 'Configs': Config.objects} 
       #return render_to_response('config/index.html', params, context_instance=RequestContext(request))
       return HttpResponseRedirect('config/')
   else:
       return HttpResponseRedirect('/login')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
