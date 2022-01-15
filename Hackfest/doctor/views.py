from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth.models import User
from .helpers import *
import uuid
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate


# Create your views here.
def choiseview(request):
    try:
        return render(request, 'choise.html' )
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")


def doctor_register(request, roleid):
    try:
        if request.method =='POST':
            uname=request.POST.get('uname',None)
            email=request.POST.get('eml',None)
            pwd=request.POST.get('pwd',None)

            if User.objects.filter(username=uname).exists():

                return HttpResponse("User already available")
            else:
                role_data=role.objects.get(role_id= roleid)
                print(role_data.role)
                user_obj=User.objects.create(username=uname,password=pwd,email=email)
                user_obj.set_password(pwd)
                user_obj.save()
                roletable= Userrolemap.objects.create(user_id=user_obj, role_id=roleid)
                roletable.save()
                messages=role_data.role
                return render (request, 'dummy.html', {"messages": messages} )
                
                
        return render(request, 'ragister.html')    
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")

def addNurse(request):
    try:
        data={'roleid': 2 , 'message': "Nurse login!!!"}

        return  render(request, 'ragister.html', context= data )
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")
def addDoctor(request):
    try:
        data={'roleid': 2 , 'message': "Doctor login!!!"}
        return  render(request, 'ragister.html', context= data )
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")

def docter_login(request):
    try:    
        if request.method =='POST':
            uname=request.POST.get('uname',None)
            pwd=request.POST.get('pwd',None)
            ubj= authenticate(request,username=uname,password=pwd)  
            q = User.objects.filter(username=uname).filter(is_staff=True)
            if q:
                print("sonthing maja aagya yaaaaa!!!!!!! ")
                return redirect("choise/" )


        
            elif ubj:
                object=Userrolemap.objects.filter(user_id=ubj).filter(role_id=2)
                if object:
                    messages="username taken thank you!!!"
                    return HttpResponse("hello nurse")
                else:
                    return HttpResponse('Hello Doctor')

            else:
                messages="Please enter valid details!!!"
                return render( request, 'index.html', {"messages": messages})

        else:
            messages="Hello, Friend! "

            return render(request, 'index.html', {"messages": messages})
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")






def doctor_logout(request):
    try:
        del request.session['uid']
        return redirect('/doctor/loginpage')
    except:
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")




