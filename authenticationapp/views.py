from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView


class Index(TemplateView):
    template_name = 'authenticationapp/index.html'


def index(request):
    return render(request, 'authenticationapp/index.html')
