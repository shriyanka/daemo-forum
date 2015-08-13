from ..models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
	category_set = serializers.PrimaryKeyRelatedField(many = True,read_only=True)
	#TODO Recursive field for category_set

	class Meta:
		model = Category
		fields = ("parent", "title", "description", "is_closed", "is_removed","category_set")
	#TODO If category has children and its parent is being updated then show error.
