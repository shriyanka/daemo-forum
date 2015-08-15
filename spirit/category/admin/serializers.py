from ..models import Category
from rest_framework import serializers
class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ("parent", "title", "description", "is_closed", "is_removed")
class CategorySerializer(serializers.ModelSerializer):
	category_set = SubCategorySerializer(many = True, read_only = True)
	class Meta:
		model = Category
		fields = ("parent", "title", "description", "is_closed", "is_removed","category_set")
	#TODO If category has children and its parent is being updated then show error.
