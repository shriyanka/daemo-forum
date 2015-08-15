from rest_framework import viewsets
from models import Category
from serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
