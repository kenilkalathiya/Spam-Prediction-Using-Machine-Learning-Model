from django.shortcuts import render

def index(request):
    params = {"request" :request, "btns": True, "home":True}
    return render(request, 'index.html', params)