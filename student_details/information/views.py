from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


@api_view(['GET'])
def student(request):
    query_set = Student.objects.all()
    serializer = StudentSerializer(query_set, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_student(request):
    query_set = Student.objects.all()
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def put_student(request, id):
    query_set = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=query_set, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_student(request,id):
    query_set = Student.objects.get(id=id)
    query_set.delete()
    return Response('one record is deleted')
