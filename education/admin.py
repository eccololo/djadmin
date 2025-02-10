from django.contrib import admin
from .models import Course, Lecture

class CourseAdmin(admin.ModelAdmin):

    prepopulated_fields = { "slug": ("course_title", ) }


admin.site.register(Course, CourseAdmin)

class LectureAdmin(admin.ModelAdmin):

    prepopulated_fields = { "slug": ("lecture_name", ) }


admin.site.register(Lecture, LectureAdmin)