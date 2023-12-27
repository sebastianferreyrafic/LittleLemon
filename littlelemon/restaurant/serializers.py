from rest_framework.serializers import ModelSerializer
from .models import MenuItem
class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'description', 'category']
