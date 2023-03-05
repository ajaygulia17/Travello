from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['your_email']
        pwd = request.POST['password']

        user = User.objects.create_user(first_name= first_name, last_name=last_name, username=username, email=email, password=pwd)
        user.save()
        return redirect("login")
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=username, password=pwd)
        if user==None:
            print("user is none")
            return redirect('login')
        auth.login(request, user)
        return redirect("/")
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
