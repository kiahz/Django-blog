from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def sing_up_views (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created successfully')
            #login
            return redirect ('articles:List')
    else:
        form = UserCreationForm()
        return render(request,'accounts/sing_up.html',{'form':form})
