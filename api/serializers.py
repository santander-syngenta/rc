from rest_framework import serializers
from .models import *


class FormSerializer(serializers.ModelSerializer):
	serializers.DateField(format='%b %d, %Y', input_formats=['%b %d, %Y'])
	class Meta:
		model = Form
		fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormTags
		fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
	serializers.DateField(format='%b %d, %Y', input_formats=['%b %d, %Y'])
	class Meta:
		model = Link
		fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
	serializers.DateField(format='%b %d, %Y', input_formats=['%b %d, %Y',])
	class Meta:
		model = Content
		fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Subject
		fields = '__all__'


class Form2Serializer(serializers.ModelSerializer):
	serializers.DateField(format='%b %d, %Y', input_formats=['%b %d, %Y',])
	class Meta:
		model = Form2
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	serializers.DateField(format='%b %d, %Y', input_formats=['%b %d, %Y',])
	class Meta:
		model = Contact
		fields = '__all__'