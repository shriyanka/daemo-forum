from models import Category
from rest_framework import serializers
class SubCategorySerializer(serializers.ModelSerializer):
	topic_set = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
	class Meta:
		model = Category
		fields = ("id","parent", "title", "description", "is_closed", "is_removed","topic_set")
class CategorySerializer(serializers.ModelSerializer):
	category_set = SubCategorySerializer(many = True, read_only = True)
	topic_set = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
	class Meta:
		model = Category
		fields = ("id","parent", "title", "description", "is_closed", "is_removed","category_set","topic_set")
		read_only_fields = ("id","is_closed","is_removed")

	#TODO disable update in these serializers
	#TODO filtering, ordering and pagination etc according to views.py
