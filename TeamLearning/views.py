from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from TeamLearning.forms import CustomUserCreationForm
from TeamLearning.site_forms import LoginForm

@csrf_protect
def login_view(request):
    print(1)
    if request.method == 'POST':
        print(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')


def logout_view(request):
    auth_logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print(1)
            form.save()
        else:
            return render(request, 'TeamLearning/signup.html', {'form': form})
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        my_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=my_password)
        login(request, user)
        return redirect('/')
    else:
        if request.user.username != '':
            return redirect('/')
        form = CustomUserCreationForm()
        return render(request, 'TeamLearning/signup.html', {'form': form})


def index_view(request):
    form = LoginForm()
    if request.method == 'GET':
        form = LoginForm()
    return render(request, 'TeamLearning/index.html', {"form": form})
