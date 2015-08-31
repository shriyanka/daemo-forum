from rest_framework import viewsets
from models import Topic
from ..comment.serializers import CommentSerializer
from serializers import TopicSerializer
from rest_framework.decorators import detail_route,list_route
from rest_framework.response import Response

class TopicViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	@detail_route(methods = ['GET'])
	def comments(self,request,**kwargs):
		comments = self.get_object().comment_set.all()
		serializer = CommentSerializer(comments, many=True)
		return Response(serializer.data)
