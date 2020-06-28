from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,DetailView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from course.models  import Course,QuestionAnswer
from trainer.models import Trainer
from .forms import CourseForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
class CourseCreate(LoginRequiredMixin,CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_register.html'
    success_url = reverse_lazy("home")
    def post(self, request):
        # Retrieve POST parameters
        name = request.POST.get('Name', '')
        description = request.POST.get('Description', '')
        Number_of_Sessions = request.POST.get('Number_of_Sessions', '')
        Course_Content = request.POST.get('Course_Content', '')
        status = request.POST.get('status', '')

        if request.POST.get('Start_date') and request.POST.get('Price'):
            Start_date = request.POST.get('Start_date','')
            Price = request.POST.get('Price','')
            Course.objects.create(
                    Name=name,
                    Description=description,
                    Number_of_Sessions=Number_of_Sessions,
                    Course_Content=Course_Content,
                    Price=Price,
                    Start_date=Start_date,
                    Status=status
                )
        elif request.POST.get('Price'):
            Price = request.POST.get('Price','')
            Course.objects.create(
                    Name=name,
                    Description=description,
                    Number_of_Sessions=Number_of_Sessions,
                    Course_Content=Course_Content,
                    Price=Price,
                    Status=status
                )
        elif request.POST.get('Start_date'):
            Start_date = request.POST.get('Start_date','')
            Course.objects.create(
                    Name=name,
                    Description=description,
                    Number_of_Sessions=Number_of_Sessions,
                    Course_Content=Course_Content,
                    Start_date=Start_date,
                    Status=status
                )
        else:
            Course.objects.create(
                    Name=name,
                    Description=description,
                    Number_of_Sessions=Number_of_Sessions,
                    Course_Content=Course_Content,
                    Status=status
                )
        return HttpResponseRedirect('success/')

class SuccessPage(TemplateView):
    template_name="success.html"


class CourseDetails(DetailView):
    model=Course
    template_name='course_detail.html'

class CourseUpdateView(LoginRequiredMixin,UpdateView):

    template_name="course_edit.html"
    success_url = reverse_lazy('home')

    form_class = CourseForm
    model = Course
class CourseDeleteView(LoginRequiredMixin,DeleteView):
    model = Course
    success_url = reverse_lazy('home')
    template_name="course_confirm_delete.html"


def add_trainer_to_course(request):
    trainers=Trainer.objects.all()
    courses=Course.objects.all()
    if request.method == "POST":
        trainer_post=request.POST.get('trainer')
        course_post=request.POST.get('course')

        course=Course.objects.get(Name=course_post)
        trainer=Trainer.objects.get(Name=trainer_post)
        course.Trainer=trainer
        course.save()
        return redirect('home')

    return render(request, 'add_trainer_to_course.html', {'trainers': trainers,'courses':courses})



def add_question_to_course(request,pk):
    course = get_object_or_404(Course,pk=pk)
    if request.method == "POST":
        question=request.POST.get('question')
        # QuestionAnswer.objects.create(
        # question=question
        # )
        question=QuestionAnswer(question=question,course=course)
        question.save()

        return redirect('home')

    return render(request, 'add_question_to_course.html')
