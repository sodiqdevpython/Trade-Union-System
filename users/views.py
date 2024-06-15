from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from users import models, serializers


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
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.filter(user=request.user).first()
            token.delete()
            return Response({"message": "Siz saytdan chiqib ketdingiz."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Bunaqa token yo'q"}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView):
    # queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
