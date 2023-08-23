from rest_framework.views import APIView
from django.db.models import Count, Max, Min, Sum
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, time
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

    def get(self, request, format=None):
        method = request.query_params.get('method')

        if method == 'in_bulk':
            primary_keys = [1, 2, 3]
            songs_dict = Song.objects.in_bulk(primary_keys)
            serialized_data = SongSerializer(songs_dict.values(), many=True)
            return Response(serialized_data.data)

        elif method == 'iterator':
            songs = Song.objects.iterator()
            serialized_data = SongSerializer(songs, many=True).data
            return Response({'message': 'Using iterator()', 'data': serialized_data})

        elif method == 'latest':
            latest_song = Song.objects.latest('release_date')
            serializer = SongSerializer(latest_song)
            return Response({'message': 'Using latest()', 'data': serializer.data})

        elif method == 'earliest':
            earliest_song = Song.objects.earliest('release_date')
            serializer = SongSerializer(earliest_song)
            return Response({'message': 'Using earliest()', 'data': serializer.data})

        elif method == 'first':
            first_song = Song.objects.first()
            serializer = SongSerializer(first_song)
            return Response({'message': 'Using first()', 'data': serializer.data})

        elif method == 'last':
            last_song = Song.objects.last()
            serializer = SongSerializer(last_song)
            return Response({'message': 'Using last()', 'data': serializer.data})

        elif method == 'aggregate':
            aggregation_data = Song.objects.aggregate(
                song_count=Count('id'),
                max_duration=Max('release_date'),
                min_duration=Min('release_date')
            )
            return Response({'message': 'Using aggregate()', 'data': aggregation_data})

        elif method == 'in_bulk':
            songs_dict = Song.objects.in_bulk()
            serialized_data = SongSerializer(songs_dict.values, many=True)
            return Response(serialized_data.data)

        elif method == 'reverse':
            song_desc = Song.objects.order_by('-release_date')
            reverse_songs = song_desc.reverse()
            serialized_data = SongSerializer(reverse_songs, many=True)
            return Response(serialized_data.data)

        elif method == 'contains':
            songs = Song.objects.filter(song_name__contains='mray mehboob')
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'icontains':
            songs = Song.objects.filter(song_name__icontains='MRAY MEHBOOB')
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'date':
            target_date = datetime(2022, 5, 4).date()
            songs = Song.objects.filter(release_date=target_date)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'day':
            songs = Song.objects.filter(release_date__day=7)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'endswith':
            songs = Song.objects.filter(song_name__endswith='you')
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'iendswith':
            songs = Song.objects.filter(song_name__iendswith='You')
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'exact':
            songs = Song.objects.filter(artist__exact='Adele')
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'iexact':
            songs = Song.objects.filter(artist__iexact='adele')
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'in':
            artists = ['atif', 'mehroz']
            songs = Song.objects.filter(artist__in=artists)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'isnull':
            songs = Song.objects.filter(artist__isnull=True)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'gt':
            target_date = date(2021, 1, 1)
            songs = Song.objects.filter(release_date__gt=target_date)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'gte':
            target_date = date(2021, 1, 1)
            songs = Song.objects.filter(release_date__gte=target_date)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'hour':
            songs = Song.objects.filter(release_date__hour=12)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'time':
            target_time = time(12, 0, 0)
            songs = Song.objects.filter(release_date__time=target_time)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'week':
            target_week = 6
            songs = Song.objects.filter(release_date__week=target_week)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'week_day':
            target_week_day = 2  # Monday = 0, Sunday = 6
            songs = Song.objects.filter(release_date__week_day=target_week_day)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'iso_week_day':
            target_iso_week_day = 5  # Monday = 1, Sunday = 7
            songs = Song.objects.filter(release_date__iso_week_day=target_iso_week_day)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'year':
            target_year = 2023
            songs = Song.objects.filter(release_date__year=target_year)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'iso_year':
            target_iso_year = 2023
            songs = Song.objects.filter(release_date__iso_year=target_iso_year)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'regex':
            target_pattern = r'^atif.*'
            songs = Song.objects.filter(song_name__regex=target_pattern)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)

        elif method == 'iregex':
            target_pattern = r'^rock.*'
            songs = Song.objects.filter(song_name__iregex=target_pattern)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)
        else:
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
