from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from .forms import *
from django.contrib.auth import get_user_model

User=get_user_model()


"""
We use the same view which published the form, i.e.. GET and POST together, allowing reusability.
For GET, we create the form to be rendered, as what should happen when we visit the URL.
For POST, the view recreates the form, populates it with the data from the request 'data binding' by RegForm(request.POST)
"""
class UserRegistrationView(View):
    def get(self,request):
        context={
            "registration_form":RegistrationForm()
        }
        return render(request,'registration_form.html',context=context)

    def post(self,request):
        reg_form=RegistrationForm(request.POST)
        if reg_form.is_valid():
            username=reg_form.cleaned_data.get('username')
            email=reg_form.cleaned_data.get('email')
            password=reg_form.cleaned_data.get('password')
            new_user=User.objects.create_user(username=username,email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')
        else:
            context={
                "registration_form":reg_form
            }
            return render(request, 'registration_form.html', context=context)
