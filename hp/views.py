from email import message
from django.shortcuts import render
from .models import profile
from django.http import HttpResponse, JsonResponse
from hp.serializers import profile1
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# ---------------------------------------------------------------class based views------------------------------------------------------------------------------
class class1(APIView):
    def get(self,request):
        return Response({message:"hello"})

# ---------------------------------------------------------------function based views------------------------------------------------------------------------------
@api_view(['GET','POST'])
def v1(request):
    if request.method == 'GET':
        desc = profile.objects.all()
        serial = profile1(desc,many = True)
        return Response(serial.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        serial = profile1(data=data)
        if serial.is_valid(): 
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def v1_details(request,pk):
    try:
        Prof = profile.objects.get(pk=pk)
    except profile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = profile1(Prof)
        return Response(serial.data)

    elif request.method == 'PUT':
        serial = profile1(Prof, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        Prof.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# json data available in web in form of list
# context = [{"id": 1, "name": "prachi", "email1": "a@a.c", "bio": "aa"},
#            {"id": 3, "name": "a", "email1": "a2@a.c", "bio": "aa"}]

# def json(request):
#     # data =  list(profile.objects.values())
#     return JsonResponse({'context':context})

# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions
# from hp.serializers import UserSerializer, GroupSerializer 

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
