from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from config.models import Config
from config.service import get_config
import datetime
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info(request.user.is_authenticated())
    if not request.user.is_authenticated():
        return  HttpResponseRedirect('/login')
        
    if request.method == 'POST':
        # save new post
       appId = request.POST['appId']
       version = request.POST['version']
       build = request.POST['build']
       platform = request.POST['platform']
       content = request.POST['content']
       cfg = Config(appId=appId)
       cfg.platform = platform
       cfg.version = version
       cfg.build = build
       cfg.islocked = False
       cfg.last_update = datetime.datetime.now() 
       cfg.content = content
       try:
           cfg.save()
       except Exception as e:
           logger.exception(e)
     
    # Get all posts from DB
    configs = Config.objects 
    return render_to_response('index.html', {'Configs': configs},
                              context_instance=RequestContext(request))


def update(request):
    logger.info(request.user.is_authenticated())
    if not request.user.is_authenticated():
        return  HttpResponseRedirect('/login')
    
    id = eval("request." + request.method + "['id']")
    cfg = Config.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        cfg.appId = request.POST['appId']
        cfg.version = request.POST['version']
        cfg.build = request.POST['build']
        cfg.platform = request.POST['platform']
        cfg.last_update = datetime.datetime.now() 
        cfg.islocked = False
        cfg.content = request.POST['content']
        cfg.save()
        template = 'index.html'
        params = {'Configs': Config.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'config':cfg}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    logger.info(request.user.is_authenticated())
    if not request.user.is_authenticated():
       return  HttpResponseRedirect('/login')
    
    id = eval("request." + request.method + "['id']")
    if request.method == 'POST':
        cfg = Config.objects(id=id)[0]
        cfg.delete() 
        template = 'index.html'
        params = {'Configs': Config.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))

def lock(request):
    logger.info(request.user.is_authenticated())
    if not request.user.is_authenticated():
       return  HttpResponseRedirect('/login')
    
    id = eval("request." + request.method + "['id']")
    if request.method == 'POST':
        cfg = Config.objects(id=id)[0]
        cfg.islocked = True
        cfg.save()
        template = 'index.html'
        params = {'Configs': Config.objects} 
    elif request.method == 'GET':
        template = 'lock.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))

def copy(request):
    logger.info(request.user.is_authenticated())
    if not request.user.is_authenticated():
       return  HttpResponseRedirect('/login')
    
    id = eval("request." + request.method + "['id']")    
    if request.method == 'POST':
        # update field values and save to mongo
       appId = request.POST['appId']
       version = request.POST['version']
       build = request.POST['build']
       platform = request.POST['platform']
       content = request.POST['content']
       cfg = Config(appId=appId)
       cfg.platform = platform
       cfg.version = version
       cfg.build = build
       cfg.islocked = False
       cfg.last_update = datetime.datetime.now() 
       cfg.content = content
       try:
           cfg.save()
       except Exception as e:
           logger.exception(e)
       template = 'index.html'
       params = {'Configs': Config.objects} 
    elif request.method == 'GET':
        cfg = Config.objects(id=id)[0]
        template = 'copy.html'
        params = {'config':cfg}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
