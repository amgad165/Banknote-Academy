from django.db import models
from users.models import CustomUser
from trainer.models import Trainer
# Create your models here.
class Course(models.Model):
    Name=models.CharField(max_length=255)
    Description=models.TextField(max_length=3000)
    Number_of_Sessions=models.CharField(max_length=255)
    Course_Content=models.TextField(max_length=3000)
    Price=models.IntegerField(blank=True,null=True)
    Start_date=models.DateField(blank=True,null=True)
    Image = models.URLField(blank=True,default='https://www.abprojeyonetimi.com/wp-content/uploads/2019/09/online-course-development-process-must-know-outsource.jpeg')
    Status=models.CharField(max_length=255)
    Trainer = models.ForeignKey('trainer.Trainer', related_name='course',on_delete=models.SET_NULL,blank=True, null=True)
    # applicants = models.ManyToManyField(CustomUser,through="Application",through_fields=('course', 'user'))

    def __str__(self):
        return self.Name

class QuestionAnswer(models.Model):
    question=models.CharField(max_length=500)
    course = models.ForeignKey(Course,related_name='course_questions',on_delete=models.CASCADE)
    def __str__(self):
        return self.course.Name
