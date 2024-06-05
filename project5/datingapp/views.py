from django.shortcuts import render

def homefn(request):
    return render(request,'home.html')

def aboutfn(request):
    return render(request,'about.html')

def contactfn(request):
    return render(request,'contact.html')