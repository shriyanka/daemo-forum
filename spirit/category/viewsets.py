from rest_framework import viewsets
from models import Category
from serializers import CategorySerializer
from ..topic.serializers import TopicSerializer
from rest_framework.decorators import detail_route,list_route
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	@detail_route(methods = ['GET'])
	def topics(self,request,**kwargs):
		topics = self.get_object().topic_set.all()
		serializer = TopicSerializer(topics, many=True)
		return Response(serializer.data)
