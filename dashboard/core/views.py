from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import File
from .forms import SignUpForm

class Index(LoginRequiredMixin, View):
  template = 'index.html'
  login_url = '/login/'
  def get(self, request):
    files = File.objects.all()
    return render(request, self.template, {'files': files})

class Register(View):
  template = 'register.html'

  def get(self, request):
    form = SignUpForm()    
    return render(request, self.template, {'form': form})

  def post(self, request):
    form = SignUpForm(request.POST)

    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/login')

class Login(View):
  template = 'login.html'

  def get(self, request):
    form = AuthenticationForm()
    return render(request, self.template, {'form': form})

  def post(self, request):
    
    form = AuthenticationForm(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print("User inputted username:", username)
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      return render(request, self.template, {'form': form})
