from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	template = loader,get_template('cpleepage.html')
	names = ['甲','乙','丙']
	context = {'names':names,
	'fulltext':'how are you'}
	return HttpResponse(template.render(context, request))
	#return render(request, 'cpleepage.html')

	