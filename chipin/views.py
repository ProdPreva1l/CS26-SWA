from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='users:login')
def home(request):
    return render(request, "chipin/home.html")