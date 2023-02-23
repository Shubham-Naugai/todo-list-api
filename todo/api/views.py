from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

# Todo List API - CRUD Operations
class ToDoAPI(APIView):
    permission_classes = [IsAuthenticated]
    #create
    def post(self, request, format=None):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created','status':'success','candidate':serializer.data})
        return Response(serializer.errors)
    
    #read
    def get(self, request, format=None):
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data)
    
    #update
    def put(self, request, pk=None, format=None):
        id=int(pk)
        todo = ToDo.objects.get(pk=id)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated','status':'success','candidate':serializer.data})
        return Response(serializer.errors)
    
    def patch(self, request, pk=None, format=None):
        id=int(pk)
        todo = ToDo.objects.get(pk=id)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial updated','status':'success','candidate':serializer.data})
        return Response(serializer.errors)
    
    #delete
    def delete(self, request, pk=None, format=None):
        id=int(pk)
        todo = ToDo.objects.get(pk=id)
        todo.delete()
        return Response({'msg':'deleted','status':'success'})
