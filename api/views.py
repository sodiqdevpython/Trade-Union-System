from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from organization.models import (
    Organization,
    Event,
    Application,
    SpiritualRest,
    Accidents
)
from .serializers import (
    OrganizationSerializer,
    EventSerializer,
    ApplicationSerializer,
    SpiritualRestSerializer,
    AccidentsSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


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
        serializered = EventSerializer(
            instance=get_event, data=request.data, partial=True)
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
            serializered = ApplicationSerializer(
                get_applications, many=True).data
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
        serializered = ApplicationSerializer(
            instance=get_application, data=request.data, partial=True)
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


from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from api import serializers


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "data": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
        })


class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = serializers.SinginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request, id_card=serializer.validated_data['id_card'], password=serializer.validated_data['password'])
        if not user:
            return Response({"message": "Bunday user yo'q"}, status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
        })


class UserLogoutAPIView(generics.GenericAPIView):
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.filter(user=request.user).first()
            token.delete()
            return Response({"message": "Siz saytdan chiqib ketdingiz."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Bunaqa token yo'q"}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
