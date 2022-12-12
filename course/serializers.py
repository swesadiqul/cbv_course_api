from rest_framework import serializers
from .models import *

# class CourseSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     author = serializers.CharField(max_length=40)
#     price = serializers.IntegerField()
#     discount = serializers.IntegerField(default=0)
#     duration = serializers.FloatField()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"