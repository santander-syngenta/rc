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

	path('uploadTraining/', views.uploadTraining, name = 'uploadTraining'),
	path('content-list/', views.contentList, name = 'content-list'),
	path('content-detail/<str:pk>/', views.contentDetail, name='content-detail'),
	path('content-delete/<str:pk>/', views.contentDelete, name='content-delete'),
	path('content-update/<str:pk>/', views.contentUpdate, name='content-update'),

	path('subject-list/', views.subjectList, name = 'subject-list'),

	path('form2-list/', views.form2List, name='form2-list'),
	path('form2-detail/<str:pk>/', views.form2Detail, name='form2-detail'),
	path('form2-delete/<str:pk>/', views.form2Delete, name='form2-delete'),
	path('form2-update/<str:pk>/', views.form2Update, name='form2-update'),
	path('uploadResource/', views.uploadResourceFunc, name='uploadResource'),

	path('contact-list/', views.contactList, name='contact-list'),
	path('contact-detail/<str:pk>/', views.contactDetail, name='contact-detail'),
	path('contact-create/', views.contactCreate, name='contact-create'),
	path('contact-delete/<str:pk>/', views.contactDelete, name='contact-delete'),
	path('contact-update/<str:pk>/', views.contactUpdate, name='contact-update'),
]