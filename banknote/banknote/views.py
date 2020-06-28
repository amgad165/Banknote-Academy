from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from course.models import Course
from trainer.models import Trainer
class HomePage(ListView):
    template_name = 'index.html'
    context_object_name = 'course_list'
    model = Course
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context.update({
            'trainer_list': Trainer.objects.all(),
            'course_list': Course.objects.all(),

        })
        return context

    def get_queryset(self):
        return Trainer.objects.all()
