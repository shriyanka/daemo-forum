from models import Topic
from rest_framework import serializers
class TopicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Topic
		fields = ("title","category","user","date","last_active","is_pinned","is_globally_pinned","is_closed","is_removed","view_count","comment_count")
		read_only_fields = ("user","date","last_active","is_pinned","is_globally_pinned","is_closed","is_removed","view_count","comment_count")
