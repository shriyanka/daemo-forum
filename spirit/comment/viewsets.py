from rest_framework import viewsets
from models import Comment
from serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
	#TODO get queryset according to view in views.py
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
