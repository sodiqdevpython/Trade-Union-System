from rest_framework import serializers
from .models import (
    Organization, 
    IdCards, 
    Event,
    Application,
    SpiritualRest
    )
from .validators import validate_card_id

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'name',
            'tel_number',
            'main_image',
            'description', 
        )

class IDCardsSerializer(serializers.ModelSerializer):

    card_id = serializers.CharField(validators=[validate_card_id])

    class Meta:
        model = IdCards
        fields = (
            'card_id',
            'is_active'
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('author' ,'name', 'spend_money', 'description', 'image')

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