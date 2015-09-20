from rest_framework import viewsets
from models import Comment
from serializers import CommentSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
class CommentViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	@permission_classes((IsAuthenticated, ))
	def create(self,request,*args,**kwargs):
		comment_serializer = CommentSerializer(data = request.data)
		if comment_serializer.is_valid(raise_exception=True):
			serializer = CommentSerializer(instance = comment_serializer.create(user = request.user))
			return Response(serializer.data,status=status.HTTP_201_CREATED,headers=self.get_success_headers(serializer.data))
		else:
			return Response(topic_serializer.errors,
										status=status.HTTP_400_BAD_REQUEST)
