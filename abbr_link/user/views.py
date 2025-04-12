from django.shortcuts import render, redirect
from .forms import UserReg, UserUpdata
from django.contrib.auth.decorators import login_required

# Create your views here.

def reg(request):
    if request.method == "POST":
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserReg()
        
    return render(request, "user/reg.html", {
        "form": form
    })
    
@login_required
def profil(request):
    if request.method == "POST":
        form = UserUpdata(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdata(instance=request.user)
    return render(request, "user/profil.html", {"form": form})