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


def login(request):
	return render(request, 'blog/home.html')

def home(request):
	return render(request, 'blog/home.html')


def methods(request):
	return	render(request,'blog/methods.html')


def training(request):
	return render(request, 'blog/training.html')


def files(request):
	return render(request, 'blog/files.html')


def display(request, pk):
	url = 'http://172.20.57.135:88/api/form-detail/' + pk + '/'
	context = {'url':url}
	return render(request, 'blog/display.html', context)


def tagDB(request):
	return render(request,'blog/tag.html')


def resources(request):
	return render(request, 'blog/resources.html')


def links(request):
	return render(request, 'blog/links.html')


def blog(request):
	return HttpResponse('This will be the blog')


def search(request, pk):
	context = {'pk':pk}
	return render(request, 'blog/search.html', context)


def forms(request):
	return render(request, 'blog/forms.html')




