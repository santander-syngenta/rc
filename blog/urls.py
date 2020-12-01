from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('blog/', views.blog, name = 'blog'),
	path('files/', views.files, name='files'),
	path('train/', views.training, name = 'training'),
	path('methods/', views.methods, name= 'methods'),
	path('display/<str:pk>/', views.display, name='display'),
	path('tagDB/', views.tagDB, name = 'tagDB'),
	path('search/<str:pk>/', views.search, name = 'search'),
	path('resources/', views.resources, name='resources'),
	path('links/', views.links, name='links'),
	path('forms/', views.forms, name='forms'),
	path('login/', views.login, name='login'),
	path('trainingUpload/', views.training, name='trainingUpload')
]