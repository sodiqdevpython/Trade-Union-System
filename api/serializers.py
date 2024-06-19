from rest_framework import serializers
from organization.validators import validate_card_id
from employee.models import (
    UnderAgeChildren, 
    HandicappedDocsModel, 
    RoleNoteModel, 
    Job, 
    Employee)

from organization.models import (
    Organization, 
    IdCards, 
    Event,
    Application,
    SpiritualRest,
    Accidents
    )

class UnderAgeChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderAgeChildren
        fields = '__all__'

class HandicappedDocsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandicappedDocsModel
        fields = '__all__'

class RoleNoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleNoteModel
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

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

class AccidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidents
        fields = (
            'who', 
            'spend_money', 
            'more_info', 
            'prove', 
        )