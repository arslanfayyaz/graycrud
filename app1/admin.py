from django.contrib import admin
from .models import Teacher, University, Song, Student, StudentProfile


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_name', 'email', 'age', 'date_of_birth')


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'university_name', 'location', 'established_year', 'total_students')


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'artist', 'release_date')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'age', 'date_of_birth', 'university')


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'hobbies', 'address')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
