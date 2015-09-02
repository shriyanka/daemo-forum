from rest_framework import viewsets
from models import Topic
from ..comment.serializers import CommentSerializer
from serializers import TopicSerializer
from rest_framework.decorators import detail_route,list_route,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class TopicViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	@detail_route(methods = ['GET'])
	def comments(self,request,**kwargs):
		comments = self.get_object().comment_set.all()
		serializer = CommentSerializer(comments, many=True)
		return Response(serializer.data)

	@permission_classes((IsAuthenticated, ))
	def create(self,request,*args,**kwargs):
		topic_serializer = serializer_class(data = request.data)
		if topic_serializer.is_valid():
			instance = topic_serializer.create(user = request.user)
			return Response(instance,status=status.HTTP_201_CREATED, headers = self.get_success_headers(topic_serializer.data))
		else:
			return Response(topic_serializer.errors,
			                            status=status.HTTP_400_BAD_REQUEST)
