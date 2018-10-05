from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from Mydbase.models import TextMessage
import random

from django.template import loader
def index(request):

	t1 = TextMessage.objects.create(speaker='Michael', message='Hello, Professor!')
	t2 = TextMessage.objects.create(speaker='Pecu', message='Hello, Class!')
	t3 = TextMessage.objects.create(speaker='Domi', message='Hello, Michael!')

	msgs = TextMessage.objects.all()


	
	#template = loader.get_template('cpleepage.html')
	#names = ['甲','乙','丙']
	#message = {'踹共','說話啊!','hihi'}
	#context = { "names": names, 'fulltext': message }
	
	return render(request, 'cpleepage.html', locals())

	