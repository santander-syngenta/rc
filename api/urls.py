from django.urls import path, include, re_path
from . import views
from django.views.generic.base import TemplateView

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

	path('link-list/', views.linkList, name='link-list'),
	path('link-detail/<str:pk>/', views.linkDetail, name='link-detail'),
	path('link-create/', views.linkCreate, name='link-create'),
	path('link-delete/<str:pk>/', views.linkDelete, name='link-delete'),
	path('link-update/<str:pk>/', views.linkUpdate, name='link-update'),

	path('upload/', TemplateView.as_view(template_name='api/upload.html'), name='upload-home'),
]