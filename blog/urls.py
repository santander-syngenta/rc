from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('blog/', views.blog, name = 'blog'),
	path('files/', views.files, name='files'),
	path('train/', views.training, name = 'training'),
	path('methods/', views.methods, name= 'methods'),
	path('display/<str:pk>/', views.display, name='display'),
	path('display2/<str:pk>/', views.display2, name='display2'),
	path('display3/<str:pk>/', views.display3, name='display3'),
	path('display4/<str:pk>/', views.display4, name='display4'),
	path('tagDB/', views.tagDB, name = 'tagDB'),
	path('search/<str:pk>/', views.search, name = 'search'),
	path('search/<str:pk>/', views.search, name = 'search'),
	path('resources/', views.resources, name='resources'),
	path('links/', views.links, name='links'),
	path('forms/', views.forms, name='forms'),
	path('login/', views.login, name='login'),
	path('trainingDB/', views.trainingUpload, name='trainingDB'),
	path('resourceFormUpload/', views.resourceFormUpload, name='resourceFormUpload'),
	path('linkUpload/', views.linkUpload, name='linkUpload'),
	path('support/', views.support, name='support'),
	path('supportAdmin/', views.supportAdmin, name='supportAdmin'),
	path('calculator/', views.calculator, name='calculator'),
]