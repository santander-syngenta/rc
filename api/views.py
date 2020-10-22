from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *
from .forms import *
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Form List': '/form-list/',
		'form Detail': '/form-detail/<str:pk>/',
		'Create form': 'form-create/',
		'Update form': 'form-delete/<str:pk>/',
		'Delete form': 'form-update/<str:pk>/',

		'Tag List': '/tag-list/',
		'Tag Detail': '/tag-detail/<str:pk>/',
		'Create tag': 'tag-create/',
		'Update tag': 'tag-delete/<str:pk>/',
		'Delete tag': 'tag-update/<str:pk>/',
	}
	return Response(api_urls)

@api_view(['GET'])
def tagList(request):
	tags = FormTags.objects.all().order_by('name')
	serializer = TagSerializer(tags, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def tagDetail(request, pk):
	tags = FormTags.objects.get(id = pk)
	serializer = TagSerializer(tags, many=False)

	return Response(serializer.data)


@api_view(['POST'])
def tagCreate(request):
	serializer = TagSerializer(data=request.data, many=False)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def tagUpdate(request, pk):
	tag = FormTags.objects.get(id=pk)
	serializer = TagSerializer(instance=tag, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def tagDelete(request, pk):
	tag = FormTags.objects.get(id=pk)
	tag.delete()

	return Response('Item Successfully Deleted!')


@api_view(['GET'])
def formList(request):
	forms = Form.objects.all().order_by('title')
	serializer = FormSerializer(forms, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def formDetail(request, pk):
	forms = Form.objects.get(id = pk)
	serializer = FormSerializer(forms, many=False)

	return Response(serializer.data)


@api_view(['POST'])
def formCreate(request):
	serializer = FormSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def formUpdate(request, pk):
	form = Form.objects.get(id=pk)
	serializer = FormSerializer(instance=form, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def formDelete(request, pk):
	form = Form.objects.get(id=pk)
	form.delete()

	return Response('Item Successfully Deleted!')


def uploadForm(request):
	form = upload()

	if request.method == "POST":
		form = upload(request.POST, request.FILES)
		print('is post')
		if form.is_valid():
			print('is valid')
			form.save()
			return redirect('blog:links')

	context = {'form':form}
	return render(request, 'api/uploadForm.html',context)