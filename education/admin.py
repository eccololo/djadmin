from django.contrib import admin
from .models import Course, Lecture


# Separate admin panel for education app.
class EducationAdminSite(admin.AdminSite):

    site_header = "Education administration"

education_site = EducationAdminSite(name="education-site")

education_site.register(Course)
education_site.register(Lecture)


class InlineLecture(admin.StackedInline):

    model = Lecture
    extra = 1
    # max_num = 2


class CourseAdmin(admin.ModelAdmin):

    inlines = [InlineLecture]

    prepopulated_fields = { "slug": ("course_title", ) }

    list_display = ["course_title", "course_description", "course_heading"]

    def course_heading(self, obj):

        return obj.course_title + " - " + obj.course_description


admin.site.register(Course, CourseAdmin)

class LectureAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Lecture:", {
            "fields": ("lecture_name", "slug"),
            "description": "Lecture details"
        }),
        ("Course:", {
            "fields": ("course",),
            "description": "Course linked"
        }),
    )

    prepopulated_fields = { "slug": ("lecture_name", ) }


admin.site.register(Lecture, LectureAdmin)