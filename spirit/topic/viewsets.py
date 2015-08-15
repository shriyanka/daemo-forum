from rest_framework import viewsets
from models import Topic
from serializers import TopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
