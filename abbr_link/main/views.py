from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateLink
from .models import Link
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, "main/home.html")

def we(request):
    return render(request, "main/we.html")

class ListLink(ListView, LoginRequiredMixin):
    model = Link
    template_name = 'main/link.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ListLink, self).get_context_data(**kwargs)
        
        ctx['form'] = CreateLink()
        ctx['link'] = Link.objects.all()
        return ctx

    # Этот метод срабатывает при отправке данных из формы
    def post(self, request, *args, **kwargs):

        post = request.POST.copy()
        post['author'] = request.user
        request.POST = post

        form = CreateLink(request.POST)
        if form.is_valid():
            form.save()

        return redirect("link")