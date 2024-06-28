from rest_framework import serializers
from users.models import User
from organization.models import (
    Organization, SpiritualRest,
    Application, Accidents,
    Event,
)



class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'title',
            'phone_number',
            'image',
            'description',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('author', 'spend_money', 'description', 'image')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'title',
            'body',
            'author_application',
            'status_application',
        )


class SpiritualRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpiritualRest
        fields = '__all__'
        read_only_fields = ['author']


class AccidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidents
        fields = (
            'user',
            'spend_money',
            'more_info',
            'prove',
        )



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id_card",)


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=16, min_length=8, write_only=True)
    password2 = serializers.CharField(
        max_length=16, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("id_card",
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
            id_card=validated_data.get("id_card"),
            organization=validated_data.get("organization"),
            password=validated_data.get("password1")
        )
        return user


class SinginSerializer(serializers.Serializer):
    id_card = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=16, min_length=8)

class UserLogoutSerializer(serializers.Serializer):
    pass