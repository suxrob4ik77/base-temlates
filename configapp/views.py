from django.shortcuts import render
from .forms import SmsForm
def index(request):
    if request.method=="POST":
        form = SmsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    return render(request,'index.html')