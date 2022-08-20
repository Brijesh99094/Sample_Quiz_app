from django.shortcuts import render
from .serializers import PersonSerializer,TaskSerializer
from app1.models import *   
from rest_framework.decorators import api_view
from rest_framework.response import  Response    
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET'])
def api(request):
    api_urls = {
        'List':'person-list',
        'Detail':'person-detail/<pk>',
        'Create':'person-create',
        'Delete':'person-detail/<pk>',
        'Update':'person-detail/<pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def ListPersons(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons,many=True)
    return Response(serializer.data)




@api_view(['GET'])
def person_detail(request,pk):
    persons = Person.objects.filter(id=pk).exists()
    if persons:
        person = Person.objects.get(id=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    else:
        return Response({'message':'Person does not exist with given id'})

@api_view(['POST'])
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Person is added'})
    else:
        return Response({'message':'Error in data... person is not added'})

@api_view(['DELETE'])
def person_delete(request,pk):
    if Person.objects.filter(id=pk).exists():
        t1 = Person.objects.get(id=pk)
        t1.delete()
        return Response({'message':'Person is deleted'})
    else:
        return Response({'message':'Person does not exists with this id'})



# Task Api class based view

class TaskApi(APIView):

    def get(self,request,pk=None,format=None):
        if pk is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks,many=True)
            return Response(serializer.data)
        else:
            tasks = Task.objects.filter(id=pk).exists()
            if tasks:
                task = Task.objects.get(id=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            else:
                return Response({'message':'Task does not exist with given id'})
    
    def post(self,request,format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message':'Task not added'})
    
    def put(self,request,pk=None,format=None):
        if Task.objects.filter(id=pk).exists():
            t1 = Task.objects.get(id=pk)
            serializer = TaskSerializer(instance=t1,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'message':'Task does not Updated'})
        else:
            return Response({'message':'Task does not exists with this id'})


    def delete(self,request,pk=None,format=None):
        if Task.objects.filter(id=pk).exists():
            t1 = Task.objects.get(id=pk)
            t1.delete()
            return Response({'message':'Task is deleted'})
        else:
            return Response({'message':'Task does not exists with this id'})

    