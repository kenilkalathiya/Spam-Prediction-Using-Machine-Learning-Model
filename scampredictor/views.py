from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .Naive_Bayes import main_function

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            pw = request.POST.get('password')

            user = authenticate(request, username=username, password=pw)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        params = {"request":request}
        return render(request, 'login.html', params)

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

def signinPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Account is created for {username}")
                return redirect('login')
            else:
                messages.success(request, "Account is not created")
                params = {'form': form}
                return render(request, 'registration.html', params)


        params = { 'form' : form, "request":request}
        return render(request, 'registration.html', params)

@login_required(login_url='/login/')
def fakeNewsDetection(request):
    params = {"request": request, "btns": True, "ans": None}

    if request.method == 'POST':
        one = main_function(request.POST.get("user-input"))[0]
        two = main_function(request.POST.get("user-input"))[1]
        if 'REAL' in one and 'REAL' in two:
            ans = 'REAL'
        elif 'FAKE' in one and 'FAKE' in two:
            ans = 'FAKE'
        else:
            ans = '50% REAL, 50% FAKE'
        params = {"request": request, "btns": True, "ans": ans}
    return render(request, 'fakeNews.html', params)