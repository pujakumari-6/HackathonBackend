from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth.models import User
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
                user_obj=User.objects.create(username=uname,password=pwd,email=email)
                user_obj.set_password(pwd)
                user_obj.save()
                print(roleid)
                if roleid == 1:
                    role_data = Role.objects.filter(role='Doctor').first()
                    print(role_data.id)
                    userRole= UserroleMap.objects.create(user_id=user_obj.id, role_id=roleid)
                    userRole.save()
                    request.session["role"]=role_data.role
                    return render(request,'doctor.html', {})
                else:
                    print('inside else')
                    role_data = Role.objects.filter(role='Nurse').first()
                    # print(role_data.id)
                    userRole= UserroleMap.objects.create(user_id=user_obj.id, role_id=roleid)
                    userRole.save()
                    request.session["role"]=role_data.role
                    return render(request,'doctor.html', {})
        return render(request, 'ragister.html')    
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")

def addNurse(request):
    try:
        data={'roleid': 2 , 'message': "Register Nurse"}
        return  render(request, 'ragister.html', context= data )
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")

def addDoctor(request):
    try:
        data={'roleid': 1 , 'message': "Register Doctor"}
        return  render(request, 'ragister.html', context= data )
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")

def docter_login(request):
    try:
        if request.method =='POST':
            uname=request.POST.get('uname',None)
            pwd=request.POST.get('pwd',None)
            print(uname)
            print(pwd)
            ubj= authenticate(request, username=uname, password=pwd) 
            print(ubj.id)
            if ubj == None:
                messages="Please enter valid details!!!"
                return render( request, 'index.html', {"messages": messages})
            q = User.objects.filter(username=uname).filter(is_staff=True)
            table1_data= UserroleMap.objects.filter(user_id=ubj.id).first()
            userRole= Role.objects.filter(id=table1_data.role_id).first()
            request.session["role"]=userRole.role
            if q and ubj:
                return redirect("choise/")
            # elif ubj:
            else:
                return render( request, 'doctor.html', {})

        else:
            return render(request, 'index.html')
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")

def doctor_logout(request):
    try:
        del request.session['uid']
        return redirect('/doctor/loginpage')
    except:
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")