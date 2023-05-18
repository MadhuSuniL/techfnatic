from rest_framework import serializers
from adminpanel.models import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    img = serializers.ImageField(allow_null=True)
    class Meta:
        model = Product
        fields = ['id','title','content','img']