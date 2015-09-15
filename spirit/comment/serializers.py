from models import Comment
from ..user.serializers import UserProfileSerializer
from rest_framework import serializers
class CommentSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField()
	class Meta:
		model = Comment
		fields = ("id","user","username", "topic","comment","comment_html", "action", "date","is_removed","is_modified","ip_address",
		"modified_count","likes_count")
		read_only_fields = ("user","comment_html","action","date","is_removed","is_modified","modified_count","likes_count")

	def get_username(self,obj):
		return obj.user.username
	def create(self,**kwargs):
		comment = Comment.objects.create(user = kwargs['user'],**self.validated_data)
		return comment
