from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
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
   user = auth.authenticate(username=username, password=password)
   if user is not None:
       auth.login(request, user)
       logger.info(auth.user_logged_in)
       request.session.set_expiry(60 * 60 * 1)  # 1 hour timeout
       #params = { 'isloggedin': auth.user_logged_in, 'Configs': Config.objects} 
       #return render_to_response('config/index.html', params, context_instance=RequestContext(request))
       return HttpResponseRedirect('config/')
   else:
       return HttpResponseRedirect('/login')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
