from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


from TeamLearning.site_forms import LoginForm


def login_view(request):
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
    else:
        form = LoginForm()
        print(request.user.username)
        if request.user.username != '':
            return redirect('/')

    return render(request, 'TeamLearning/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('/')


def index_view(request):
    if request.method == 'GET':
        form = LoginForm()
    return render(request, 'TeamLearning/index.html')
