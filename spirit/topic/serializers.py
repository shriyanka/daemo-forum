from models import Topic
from ..category.serializers import CategorySerializer
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Topic
		fields = ("id","title","category","user","date","last_active","is_pinned","is_globally_pinned","is_closed","is_removed","view_count","comment_count")
		read_only_fields = ("id","user","date","last_active","is_pinned","is_globally_pinned","is_closed","is_removed","view_count","comment_count")

	def create(self,**kwargs):
		topic = Topic.objects.create(user = kwargs['user'],**self.validated_data)
		return topic

#TODO category serializer
#TODO user serializer
#TODO update, create : get user fron request
