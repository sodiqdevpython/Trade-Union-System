from rest_framework import viewsets
from .models import UnderAgeChildren, HandicappedDocsModel, RoleNoteModel, Job, Employee
from .serializers import UnderAgeChildrenSerializer, HandicappedDocsModelSerializer, RoleNoteModelSerializer, JobSerializer, EmployeeSerializer

class UnderAgeChildrenViewSet(viewsets.ModelViewSet):
    queryset = UnderAgeChildren.objects.all()
    serializer_class = UnderAgeChildrenSerializer

class HandicappedDocsModelViewSet(viewsets.ModelViewSet):
    queryset = HandicappedDocsModel.objects.all()
    serializer_class = HandicappedDocsModelSerializer

class RoleNoteModelViewSet(viewsets.ModelViewSet):
    queryset = RoleNoteModel.objects.all()
    serializer_class = RoleNoteModelSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
