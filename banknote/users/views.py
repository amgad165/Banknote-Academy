from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from  application.models import Application
# Create your views here.
class SignUp(CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'Registration.html'
    success_url = reverse_lazy("login")
class UpdateUser(LoginRequiredMixin,UpdateView):
    form_class = forms.CustomUserChangeForm
    login_url = '/login/'
    template_name = 'edit_info.html'
    success_url = reverse_lazy("home")
    model= CustomUser

@login_required
def MyApplicationList(request):
    current_user=request.user
    application_list=Application.objects.filter(user=current_user)

    return render(request, 'myapplication_list.html', {'application_list': application_list})
class MyApplicationDeleteView(LoginRequiredMixin,DeleteView):
    model = Application
    success_url = reverse_lazy('users:myapplication_list')
    template_name="confirm_delete.html"
