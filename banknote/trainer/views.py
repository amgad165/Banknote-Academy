from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,DetailView,DetailView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from trainer.models  import Trainer
from .forms import TrainerForm

class TrainerCreate(LoginRequiredMixin,CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_create.html'
    redirect_field_name = 'create_success.html'

class SuccessPage(TemplateView):
    template_name="create_success.html"

class TrainerListView(ListView):
    model = Trainer
    template_name="trainer_list.html"
    context_object_name = 'trainer_list'
class TrainerDetailView(DetailView):
    model = Trainer
    template_name="trainer_details.html"


class TrainerUpdateView(LoginRequiredMixin,UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'trainer_list.html'
    template_name="trainer_edit.html"

    form_class = TrainerForm

    model = Trainer


class TrainerDeleteView(LoginRequiredMixin,DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainer:trainer_list')
    template_name="trainer_confirm_delete.html"
