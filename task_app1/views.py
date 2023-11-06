from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from task_app1.employee import employee
from task_app1.consumer import consumer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from .serializer import *


def home(request):
    return HttpResponse("Hello world")


class EmployeeAPI(APIView):
    def get(self, request, **kwargs):
        result = employee()
        return Response(result)


class ConsumerAPI(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        category = request.data['category']
        result = consumer(category)
        return Response({
            'status': 'success',
            'data': result
        })
