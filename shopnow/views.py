from django.shortcuts import render

def home(request):
    context = {
        "message":"My name",
        "Ajay":"is Ajay",
    }
    return render(request,'home.html',context=context)


