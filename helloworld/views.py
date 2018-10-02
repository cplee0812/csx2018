from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random

from django.template import loader
def index(request):
	template = loader.get_template('cpleepage.html')
	names = ['甲','乙','丙']
	context = { "names": names, "fulltext": "說你好" }
	return render(request, 'cpleepage.html', locals())

	