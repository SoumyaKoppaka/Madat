from django.shortcuts import render
from django.views import generic

def home(request):
    return render(request, 'roles/index.html')


class SignUpView(generic.TemplateView):
    template_name = 'register.html'


def about(request):
    return render(request, 'roles/about.html')

def contact(request):
    return render(request, 'roles/contact.html')

