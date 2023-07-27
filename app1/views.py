from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import University, Teacher, Song, Student, StudentProfile
from .serializers import UniversitySerializer, TeacherSerializer, SongSerializer, StudentSerializer, StudentProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class UniversityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            university = University.objects.get(id=id)
            serializer = UniversitySerializer(university)
            return Response(serializer.data)

        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        uni = University.objects.get(pk=id)
        serializer = UniversitySerializer(uni, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete data updated'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        uni = University.objects.get(pk=id)
        serializer = UniversitySerializer(uni, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'})

        return Response(serializer.errors)

    def get_university(self, pk):
        try:
            return University.objects.get(pk=pk)
        except University.DoesNotExist:
            return None

    def delete(self, request, pk, format=None):
        university = self.get_university(pk)
        if not university:
            return Response({'error': 'University not found'}, status=status.HTTP_404_NOT_FOUND)

        university.delete()
        return Response({'msg': 'University deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class TeacherView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)

        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        teach = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(teach, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete data updated'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        teach = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(teach, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'})

        return Response(serializer.errors)

    def get_teacher(self, pk):
        try:
            return Teacher.objects.get(pk=pk)

        except Teacher.DoesNotExist:
            return None

    def delete(self, request, pk, format=None):
        teacher = self.get_teacher(pk)
        if not teacher:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return Response({'msg': 'Teacher deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class SongView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            song = Song.objects.get(id=id)
            serializer = SongSerializer(song)
            return Response(serializer.data)

        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        song = Song.objects.get(pk=id)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete data updated'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        song = Song.objects.get(pk=id)
        serializer = SongSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'})

        return Response(serializer.errors)

    def get_song(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return None

    def delete(self, request, pk, format=None):
        song = self.get_song(pk)
        if not song:
            return Response({'error': 'Song not found'}, status=status.HTTP_404_NOT_FOUND)

        song.delete()
        return Response({'msg': 'Song deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class StudentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        id = pk
        filter_params = request.query_params

        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        filtered_students = Student.objects.all()

        for param, value in filter_params.items():
            filtered_students = filtered_students.filter(**{param: value})

        serializer = StudentSerializer(filtered_students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete data updated'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'})

        return Response(serializer.errors)

    def get_student(self, pk):

        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return None

    def delete(self, request, pk, format=None):
        student = self.get_student(pk)

        if not student:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({'msg': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class StudentProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return StudentProfile.objects.get(pk=pk)
        except StudentProfile.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk=None, format=None):
        if pk is not None:
            student_profile = self.get_object(pk)
            serializer = StudentProfileSerializer(student_profile)
            return Response(serializer.data)

        student_profiles = StudentProfile.objects.all()
        serializer = StudentProfileSerializer(student_profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        student_profile = self.get_object(pk)
        serializer = StudentProfileSerializer(student_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'StudentProfile data updated'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        student_profile = self.get_object(pk)
        serializer = StudentProfileSerializer(student_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial data updated'})

        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        student_profile = self.get_object(pk)
        student_profile.delete()
        return Response({'msg': 'StudentProfile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
