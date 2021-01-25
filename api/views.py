from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, authentication_classes, parser_classes, renderer_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import MultiPartRenderer

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
		'Update form': 'form-update/<str:pk>/',
		'Delete form': 'form-delete/<str:pk>/',

		'Tag List': '/tag-list/',
		'Tag Detail': '/tag-detail/<str:pk>/',
		'Create tag': 'tag-create/',
		'Update tag': 'tag-update/<str:pk>/',
		'Delete tag': 'tag-delete/<str:pk>/',

		'Link List': '/link-list',
		'Link Detail': '/link-detail/<str:pk>/',
		'Create link':'/link-create/',
		'Update link': '/link-update/<str:pk>/',
		'Delete link': '/link-delete/<str:pk>/',

		'Training List': '/content-list',
		'Training Detail': '/training-list',
		'Update Training': '/training-update',
		'Delete Training': '/training-delete',
		'Subject List': '/subject-list',

		'Resource List':'/form2-list/',
		'Resource Detail': '/form2-detail/<str:pk>/',
		'Update Resource': '/form2-update/<str:pk>/',
		'Delete Resource': '/form2-delete/',
	}
	return Response(api_urls)


@api_view(['GET'])
def linkList(request):
	links = Link.objects.all().order_by('title')
	serializer = LinkSerializer(links, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def linkDetail(request, pk):
	link = Link.objects.get(id = pk)
	serializer = LinkSerializer(link, many=False)

	return Response(serializer.data)


@api_view(['POST'])
def linkCreate(request):
	serializer = LinkSerializer(data=request.data, many=False)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def linkUpdate(request, pk):
	link = Link.objects.get(id=pk)
	serializer = LinkSerializer(instance = link, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def linkDelete(request, pk):
	link = Link.objects.get(id=pk)
	link.delete()

	return Response('Item Successfully Deleted')


@api_view(['GET'])
def contactList(request):
	contacts = Contact.objects.all().order_by('name')
	serializer = ContactSerializer(contacts, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def contactDetail(request, pk):
	contact = Contact.objects.get(id = pk)
	serializer = ContactSerializer(contact, many = False)

	return Response(serializer.data)


@api_view(['POST'])
def contactCreate(request):
	serializer = ContactSerializer(data = request.data, many=False)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def contactUpdate(request, pk):
	contact = Contact.objects.get(id=pk)
	serializer = ContactSerializer(instance=contact, data = request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def contactDelete(request, pk):
	contact = Contact.objects.get(id=pk)
	contact.delete()

	return Response('Item Successfully Deleted!')


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
@parser_classes([MultiPartParser, FormParser])
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
		if form.is_valid():
			print('valid')
			filename = str(request.FILES['file'])
			handle_uploaded_file(request.FILES['file'], filename)
			form.save()
			return redirect('blog:files')
		else:
			print('not valid')
			
	context = {'form':form}
	return render(request, 'api/uploadForm.html',context)


def handle_uploaded_file(f, filename):
    with open('static/images/documents/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def uploadTraining(request):
	form = uploadTrainingContent()

	if request.method == "POST":
		form = uploadTrainingContent(request.POST, request.FILES)
		if form.is_valid:
			for f in request.FILES.getlist('file'):
				filename = str(f)
				handle_uploaded_content(f, filename)
			form.save()
			return redirect('blog:trainingDB')

	context = {'form':form}
	return render(request, 'api/trainingUpload.html',context)


def handle_uploaded_content(f, filename):
    with open('static/images/documents/training/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@api_view(['GET'])
def contentList(request):
	trainingContent = Content.objects.all().order_by('title')
	serializer = ContentSerializer(trainingContent, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def contentDetail(request, pk):
	trainingContent = Content.objects.get(id = pk)
	serializer = ContentSerializer(trainingContent, many = False)

	return Response(serializer.data)


@api_view(['POST'])
def contentUpdate(request, pk):
	trainingContent = Content.objects.get(id = pk)
	serializer = ContentSerializer(instance = form, data = request.data, partial = True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def contentDelete(request, pk):
	trainingContent = Content.objects.get(id = pk)
	trainingContent.delete()

	return Response('Item Successfully Deleted!')


@api_view(['GET'])
def subjectList(request):
	subjects = Subject.objects.all().order_by('name')
	serializer = SubjectSerializer(subjects, many = True)
	
	return Response(serializer.data)


@api_view(['GET'])
def form2List(request):
	forms = Form2.objects.all().order_by('title')
	serializer = Form2Serializer(forms, many=True)

	return Response(serializer.data)


@api_view(['GET'])
def form2Detail(request, pk):
	forms = Form2.objects.get(id = pk)
	serializer = Form2Serializer(forms, many=False)

	return Response(serializer.data)


@api_view(['POST'])
def form2Update(request, pk):
	form = Form2.objects.get(id=pk)
	serializer = Form2Serializer(instance=form, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def form2Delete(request, pk):
	form = Form2.objects.get(id=pk)
	form.delete()

	return Response('Item Successfully Deleted!')


def uploadResourceFunc(request):
	form = uploadResourceForm()
	if request.method == "POST":
		form = uploadResourceForm(request.POST, request.FILES)
		if form.is_valid():
			filename = str(request.FILES['file'])
			handle_uploaded_form(request.FILES['file'], filename)
			form.save()
			return redirect('blog:resourceFormUpload')

	context = {'form':form}
	return render(request, 'api/uploadResource.html',context)


def handle_uploaded_form(f, filename):
    with open('static/images/documents/resourceForms/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



