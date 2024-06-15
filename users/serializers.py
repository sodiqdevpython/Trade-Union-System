from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("full_name", "id_card", "phone_number")


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=16, min_length=8, write_only=True)
    password2 = serializers.CharField(
        max_length=16, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("full_name", "id_card", "phone_number",
                  "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1", "")
        password2 = attrs.get("password2", "")

        if password1 != password2:
            raise serializers.ValidationError(
                "1-parol va 2-parol bir xil bo'lishi kerak")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data.get("full_name"),
            id_card=validated_data.get("id_card"),
            phone_number=validated_data.get("phone_number"),
            password=validated_data.get("password1")
        )
        return user


class SinginSerializer(serializers.Serializer):
    id_card = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=16, min_length=8)

class UserLogoutSerializer(serializers.Serializer):
    pass