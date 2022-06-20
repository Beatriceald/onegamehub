from multiprocessing import AuthenticationError, context
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Urls
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .utils import *

class MainView(TemplateView):
    template_name = 'urls/index.html'

    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            urls = Urls.objects.all()
            context['urls'] = urls
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)


# def index(request):
#     context = {
#         'title': 'URL Status Checker',

#     }
#     return render(request, 'urls/index.html', context=context)
# Create your views here.

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'urls/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'urls/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Authorization')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')