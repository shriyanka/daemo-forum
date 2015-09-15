from models import UserProfile
from rest_framework import serializers
class UserProfileSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField()
	class Meta:
		model = UserProfile
		fields = ("id","username","location","last_seen","timezone","is_admiis_administrator","is_moderator","is_verified")
		read_only_fields = ("id")

	def get_username(self, obj):
		return obj.user.username

	#TODO disable update in these serializers
	#TODO filtering, ordering and pagination etc according to views.py
