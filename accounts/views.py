from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def sing_up_view (request):
    form=UserCreationForm()
    return render(request,'accounts/sing_up.html',{'form':form})