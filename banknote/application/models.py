from django.db import models
from course.models import Course
from users.models import CustomUser
from django.utils import timezone

# Create your models here.
class Application(models.Model):
    Status=models.CharField(max_length=255,null=True,blank=True,default='Waiting for apply')
    Apply_Date=models.DateTimeField(max_length=255,default=timezone.now())
    answer=models.TextField(max_length=10000,null=True,blank=True)
    course = models.ForeignKey(Course,related_name='course_applications',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,related_name='user_courses',on_delete=models.CASCADE)
    def __str__(self):
        return self.course.Name
    class Meta:
        ordering = ["-Apply_Date"]
