from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from .models import *
from .serializers import *

from api import serializers


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class ListUsers(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request):
        quizs = Quizs.objects.all()
        serializer = QuizSerializer(quizs, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        serializer = QuizSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'payload': serializer.errors, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'You have successfully Created Quiz.'})


    def put(self, request):
        pass

    def patch(self, request):
        try:
            quizs = Quizs.objects.get(id = request.data['id'])
            serializer = QuizSerializer(quizs, data = request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'payload': serializer.errors, 'message': 'Something went wrong'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'You have successfully Created Quiz.'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid ID'})


    def delete(self, request):
        try:
            id = request.GET.get('id')
            quizs = Quizs.objects.get(id=id)
            quizs.delete()
            return Response({'status': 200, 'message': 'Quiz Successfully deleted'})
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid ID'})