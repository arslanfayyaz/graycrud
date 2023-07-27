from rest_framework import serializers
from .models import Teacher, University, Song, Student, StudentProfile


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    university = serializers.PrimaryKeyRelatedField(queryset=University.objects.all(), required=False)

    class Meta:
        model = Student
        fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):

    student = StudentSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['bio', 'hobbies', 'address', 'student']



