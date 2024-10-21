from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout

def sing_up_views (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #login

            return redirect ('articles:List')
    else:
        form = UserCreationForm()
    return render(request,'accounts/sing_up.html',{'form':form})

def login_view (request):
    if request.method == "POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()
            login(request, user)
            return redirect('articles:List')
    else:
        form=AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})


def logout_view (request):
    if request.method == "POST":
        logout(request)
        return redirect('articles:List')
