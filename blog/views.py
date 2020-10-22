from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
# Create your views here.
from .models import *
from api.models import *
from api.serializers import *
from django.views.decorators.clickjacking import xframe_options_exempt


def home(request):
	return render(request, 'blog/home.html')


def methods2(request):
	return	render(request,'blog/methods2.html')


def training(request):
	return render(request, 'blog/training.html')


def links(request):
	return render(request, 'blog/link.html')

@xframe_options_exempt
def display(request, pk):
	url = 'http://127.0.0.1:8080/api/form-detail/' + pk + '/'
	context = {'url':url}
	return render(request, 'blog/display.html', context)


def tagDB(request):
	return render(request,'blog/tag.html')


def blog(request):
	return HttpResponse('This will be the blog')





