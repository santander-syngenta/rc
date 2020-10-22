from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.apiOverview, name='api-overview'),

	path('tag-list/', views.tagList, name='tag-list'),
	path('tag-detail/<str:pk>/', views.tagDetail, name='tag-detail'),
	path('tag-create/', views.tagCreate, name='tag-create'),
	path('tag-delete/<str:pk>/', views.tagDelete, name='tag-delete'),
	path('tag-update/<str:pk>/', views.tagUpdate, name='tag-update'),

	path('form-list/', views.formList, name='form-list'),
	path('form-detail/<str:pk>/', views.formDetail, name='form-detail'),
	path('form-create/', views.formCreate, name='form-create'),
	path('form-delete/<str:pk>/', views.formDelete, name='form-delete'),
	path('form-update/<str:pk>/', views.formUpdate, name='form-update'),

	path('uploadForm/', views.uploadForm, name = 'uploadForm'),
]