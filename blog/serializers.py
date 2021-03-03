from rest_framework import serializers
from .models import School, Group, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('number', "address")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('number', 'profile_group', 'school')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age', 'group')
