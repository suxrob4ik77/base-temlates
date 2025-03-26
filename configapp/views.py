from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .forms import SmsForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    if request.method=="POST":
        form = SmsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    return render(request,'index.html')




def loginPage(request):
    form = UserLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Muvaffaqiyatli tizimga kirdingiz!")
            return redirect('home')
        else:
            messages.error(request, "Noto‘g‘ri username yoki parol!")

    return render(request, 'login.html', {'form': form})


def logoutPage(request):
    logout(request)
    return redirect('login')