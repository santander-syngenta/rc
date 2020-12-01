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