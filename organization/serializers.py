from rest_framework import serializers
from .models import (
    Organization,
    Event,
    Application,
    SpiritualRest,
    Accidents
)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'name',
            'tel_number',
            'main_image',
            'description',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('author', 'name', 'spend_money', 'description', 'image')


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
            'who',
            'spend_money',
            'more_info',
            'prove',
        )
