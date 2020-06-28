from django.contrib import admin

# Register your models here.

from .models import Course,QuestionAnswer

admin.site.register(Course)
admin.site.register(QuestionAnswer)
