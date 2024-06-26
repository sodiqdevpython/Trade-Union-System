from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from employee.models import (
        Job, 
        Employee,
        RoleNoteModel, 
        UnderAgeChildren, 
        HandicappedDocsModel,
    )

from organization.models import (
        Event,
        IdCards,
        Accidents,
        Application,
        Organization,
        SpiritualRest,
    )

from .serializers import (
        JobSerializer, 
        EventSerializer,
        IDCardsSerializer,
        EmployeeSerializer,
        AccidentsSerializer,
        ApplicationSerializer,
        OrganizationSerializer,
        SpiritualRestSerializer,
        RoleNoteModelSerializer,
        UnderAgeChildrenSerializer, 
        HandicappedDocsModelSerializer, 
    )

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


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class IDCardViewSet(viewsets.ModelViewSet):
    queryset = IdCards.objects.all()
    serializer_class = IDCardsSerializer

class EventView(APIView):

    def get(self, request, id=None):
        if id:
            event_data = get_object_or_404(Event, id=id)
            serializered = EventSerializer(event_data)
        else:
            event_data = Event.objects.all()
            serializered = EventSerializer(event_data, many=True)

        return Response(serializered.data)

    def post(self, request):
        get_data = request.data
        serializered = EventSerializer(data=get_data)
        if serializered.is_valid():
            serializered.save(author=request.user)

            return Response({
                'status': 'ok',
                'result': serializered.data
            })
        else:
            return Response({
                'status': 'error',
                'error details': serializered.errors
            })
    
    def patch(self, request, id):
        get_event = get_object_or_404(Event, id=id)
        serializered = EventSerializer(instance=get_event, data=request.data, partial=True)
        if serializered.is_valid():
            serializered.save()
            return Response({
                'status': 'ok',
                'result': serializered.data
            })
        else:
            return Response({
                'status': 'error',
                'error details': serializered.errors
            })

class ApplicationView(APIView):

    def get(self, request, id=None):
        if id:
            get_application = get_object_or_404(Application, id=id)
            return Response(
                ApplicationSerializer(
                    get_application
                ).data
            )
        else:
            get_applications = Application.objects.all()
            serializered = ApplicationSerializer(get_applications, many=True).data
            return Response(serializered)

    def post(self, request):
        get_data = request.data
        serializered = ApplicationSerializer(data=get_data)
        if serializered.is_valid():
            serializered.save(author_application=request.user.employee_user)
            return Response({
                'status': 'ok',
                'result': serializered.data 
            })
        else:
            return Response({
                'status': 'error',
                'error message': serializered.errors
            })

    def patch(self, request, id):
        get_application = get_object_or_404(Application, id=id)
        serializered = ApplicationSerializer(instance=get_application, data=request.data, partial=True)
        if serializered.is_valid():
            serializered.save()
            return Response({
                'status': 'ok',
                'result': serializered.data
            })
        else:
            return Response({
                'error message': serializered.errors
            })
        
class SpiritualRestView(viewsets.ModelViewSet):
    queryset = SpiritualRest.objects.all()
    serializer_class = SpiritualRestSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.employee_user)

class AccidentsView(viewsets.ModelViewSet):
    queryset = Accidents.objects.all()
    serializer_class = AccidentsSerializer