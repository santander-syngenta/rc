from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('blog/', views.blog, name = 'blog'),
	path('links/', views.links, name='links'),
	path('train/', views.training, name = 'training'),
	path('methods2/', views.methods2, name= 'methods2'),
	path('display/<str:pk>/', views.display, name='display'),
	path('tagDB/', views.tagDB, name = 'tagDB')
]