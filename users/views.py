from django.contrib.auth import login
from django.shortcuts import redirect, render
from users.forms import RegiterUserCreationForm
from django.contrib import messages

def register(request): 
    form = RegiterUserCreationForm(request.POST or None)
    if  request.method == "POST":        
        if  form.is_valid():
            user = form.save()
            login(request, user)            
            return redirect("dwitter:profile_list")
       
    
    return render(request,"users/register.html",{"form":form})
  


