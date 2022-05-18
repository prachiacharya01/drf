from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from hp.models import profile

class profile1(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ['id','name','email1','bio']
        
    # name = serializers.CharField(max_length= 50) 
    # email1 = serializers.CharField(max_length = 50)
    # bio = serializers.CharField(max_length=50)

    # def create(self, validated_data):
    #     return profile1.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email1 = validated_data.get('email1',instance.email1)
    #     instance.bio = validated_data.get('bio',instance.bio)
    #     instance.save()
    #     return instance 
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


