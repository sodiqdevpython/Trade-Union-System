from rest_framework import serializers
from .models import UnderAgeChildren, HandicappedDocsModel, RoleNoteModel, Job, Employee

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
