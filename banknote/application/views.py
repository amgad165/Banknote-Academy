from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,DetailView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from course.models import QuestionAnswer,Course
from application.models  import Application
from users.models import CustomUser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

class ApplicationList(LoginRequiredMixin,ListView):
    model=Application
    template_name = 'application_list.html'

class AcceptedList(LoginRequiredMixin,ListView):
    model=Application
    template_name = 'accepted_list.html'
class ApplicationDetails(LoginRequiredMixin,DetailView):
    model=Application
    template_name='application_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context

        context = super().get_context_data(**kwargs)
        application=Application.objects.get(pk=self.kwargs['pk'])
        course=application.course
        questions=course.course_questions.all()
        # Add in a QuerySet of all the books
        context['questions'] = questions
        return context
class ApplicationDeleteView(LoginRequiredMixin,DeleteView):
    model = Application
    success_url = reverse_lazy('application:applicants_list')
    template_name="confirm_delete.html"

class AlreadyEnrolled(LoginRequiredMixin,TemplateView):
    template_name='already.html'

class EmailView(LoginRequiredMixin,TemplateView):
    template_name='email_sent.html'



@login_required
def application(request,pk):
    questions=QuestionAnswer.objects.filter(course__pk=pk)
    course=Course.objects.get(pk=pk)
    current_user=request.user

    # courses=Course.objects.all()
    if request.method == "POST":
        num_results = Application.objects.filter(course=course,user=current_user).count()
        if num_results >= 1:
            return redirect('application:already')
        else:
            answer=request.POST.getlist('answer')
            application=Application(course=course,user=current_user,answer=answer)
            application.save()

            return redirect('application:email_sent')

    return render(request, 'application.html', {'questions': questions})


def ApplicationApply(request,pk):
    application=Application.objects.get(pk=pk)
    application.Status="Accepted"
    application.save()
    send_mail(
        'Banknote Academy '+ application.course.Name+' Course',
            'I hope this e-mail finds you well,'+'\n'+'You have been Accepted for '+application.course.Name+ ' Course' +'\n'+
            'Best Regards',
        'banknoteacademy2020@gmail.com',
        [application.user.email],
        fail_silently=False,
    )
    return redirect('application:applicants_list')
