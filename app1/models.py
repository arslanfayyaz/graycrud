from django.db import models


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.teacher_name


class University(models.Model):
    university_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    established_year = models.IntegerField()
    total_students = models.IntegerField()
    teachers = models.ManyToManyField(Teacher, related_name='universities', blank=True, null=True)

    def __str__(self):
        return self.university_name


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.song_name


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students', blank=True, null=True)
    songs = models.ManyToManyField(Song, related_name='students', blank=True, null=True)

    def __str__(self):
        return self.student_name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    hobbies = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"student hobbies are {self.hobbies}"
