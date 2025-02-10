from django.db import models


class Course(models.Model):

    course_title = models.CharField(max_length=100)
    course_description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=100)


class Lecture(models.Model):

    lecture_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)