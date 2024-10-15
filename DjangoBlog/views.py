from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
   # return HttpResponse('hi there fuck u')
    return render(request,'about.html')
def home(request):
   # return HttpResponse('Wellcome to DjangoBlog')
    return render(request,'home.html')

def contact(request):
   #return HttpResponse('my phone number : 09155966630')
    return render(request,'contact.html')

def blog(request):
   #return HttpResponse('hichi nis')
    return render(request,'blog.html')