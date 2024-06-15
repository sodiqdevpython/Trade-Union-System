from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from employee import models as emodel
from .serializers import EmployeeSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class EmployeeView(APIView):

    def get(self, request):
        get_employee = emodel.Employee.objects.all()
        serializered = EmployeeSerializer(get_employee, many=True)
        context = {
            'data': serializered.data
        }

        return Response(context)
    

