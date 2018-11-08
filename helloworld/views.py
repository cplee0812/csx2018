from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from Mydbase.models import TextMessage
import random
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from .forms import nameForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
@csrf_protect
def index(request):
    if request.method == 'POST': #是否为post请求
        form=nameForm(request.POST)
        ans={}
        ans['response']='還敢進來啊冰鳥!!'  
        return render(request,'certification.html',ans) 
    else:return render(request, 'certification.html', locals())


def mainpage(request):



	if request.method == 'POST':
		if request.user.is_authenticated:
			_speaker = request.user.username
		_message = request.POST.get('msg')
		TextMessage.objects.create(speaker=_speaker, message=_message)
		
	msgs = TextMessage.objects.all()	

	if request.method == 'GET':
		if request.user.is_authenticated:
			if request.GET.get('keywords') is not None:
				msg_search = request.GET.get('keywords')
				msgs = TextMessage.objects.filter(message__icontains= msg_search)
	return render(request, 'cpleepage.html', locals())

def personal(request):

	if request.user.is_authenticated:
		_user = request.user
		msgs = TextMessage.objects.filter(speaker= _user)
	return render(request, 'mypage.html', locals())

def deletemsg(request):

	return render(request, 'mypage.html', locals())

def about(request):

	return render(request, 'about.html', locals())
	