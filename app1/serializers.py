from rest_framework import serializers
from .models import Teacher, University, Song, Student, StudentProfile


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    # teachers = TeacherSerializer(many=True, read_only=True)
    # teacher = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='teachers')

    class Meta:
        model = University
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


# class StudentSerializer(serializers.ModelSerializer):
#     university = UniversitySerializer()
#     songs = SongSerializer(many=True)
#
#     class Meta:
#         model = Student
#         fields = '__all__'
#
#     def create(self, validated_data):
#         university_data = validated_data.pop('university', None)
#         song_data = validated_data.pop('songs', [])
#
#         student = Student.objects.create(**validated_data)
#
#         if university_data:
#             university = University.objects.create(**university_data)  # Create a new University object
#             student.university = university
#
#
#         return student


class StudentSerializer(serializers.ModelSerializer):
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='songs')
    university = serializers.PrimaryKeyRelatedField(queryset=University.objects.all(), required=False)
    # university = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='universitys')

    class Meta:
        model = Student
        fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):

    student = StudentSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['bio', 'hobbies', 'address', 'student']



