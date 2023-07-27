# Generated by Django 4.2.3 on 2023-07-26 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('established_year', models.IntegerField()),
                ('total_students', models.IntegerField()),
                ('teachers', models.ManyToManyField(blank=True, null=True, related_name='universities', to='app1.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('songs', models.ManyToManyField(blank=True, null=True, related_name='students', to='app1.song')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app1.university')),
            ],
        ),
    ]
