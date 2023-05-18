from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %I:%M %p')
    class Meta:
        model = User
        fields = ['id','username','password','date_joined']