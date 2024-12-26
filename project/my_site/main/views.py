from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')
def epoch1(request):
    return render(request,'main/epoch1.html')
def epoch2(request):
    return render(request,'main/epoch2.html')
def epoch3(request):
    return render(request,'main/epoch3.html')
def epoch4(request):
    return render(request,'main/epoch4.html')
def collection1(request):
    return render(request,'main/collection1.html')
def collection2(request):
    return render(request,'main/collection2.html')
def collection3(request):
    return render(request,'main/collection3.html')
def collection4(request):
    return render(request,'main/collection4.html')
