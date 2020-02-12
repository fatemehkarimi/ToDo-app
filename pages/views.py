from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from datetime import date
from django.urls import reverse_lazy

from .forms import ToDo_objCreateForm, ToDo_objUpdateForm
from .models import ToDo_obj

# Create your views here.
class HomePageView(ListView):
    model = ToDo_obj
    template_name = 'home.html'


class ToDo_objCreateView(CreateView):
    model = ToDo_obj
    form_class = ToDo_objCreateForm
    template_name = 'todo_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.create_date = date.today()
        return super().form_valid(form)

class ToDo_objUpdateView(UpdateView):
    model = ToDo_obj
    form_class = ToDo_objUpdateForm
    template_name = 'todo_update.html'
    success_url = reverse_lazy('home')