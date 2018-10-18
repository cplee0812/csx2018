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
@csrf_protect
def index(request):
    if request.method == 'POST': #是否为post请求
        form=nameForm(request.POST)
        ans={}
        ans['response']='還敢進來啊冰鳥!!'  
        return render(request,'certification.html',ans) 
    else:return render(request, 'certification.html', locals())


def mainpage(request):

	t1 = TextMessage.objects.create(speaker='Michael', message='Hello, Professor!')
	t2 = TextMessage.objects.create(speaker='Pecu', message='Hello, Class!')
	t3 = TextMessage.objects.create(speaker='Domi', message='Hello, Michael!')

	msgs = TextMessage.objects.all()


	
	#template = loader.get_template('cpleepage.html')
	#names = ['甲','乙','丙']
	#message = {'踹共','說話啊!','hihi'}
	#context = { "names": names, 'fulltext': message }
	
	return render(request, 'cpleepage.html', locals())

	