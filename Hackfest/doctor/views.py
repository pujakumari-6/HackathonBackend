from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from .models import Prescription, PrescribedMedicine, Medicine
from healthcare.models import Patient, PatientRecord
from django.contrib.auth.models import User


# Create your views here.
def view_login(request):
    return render(request, 'index.html')


def docter_login(request):
    try:
        uname=request.POST.get('uname',None)
        pwd=request.POST.get('pwd',None)
        ubj= User.objects.filter(username=uname).first()
        if ubj:
            request.session['uid']= request.POST['uname']
            return HttpResponse("Logged in...")
        else:
            return HttpResponse("Invalid creadentials...")
    except:
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")
    #  vlidate session use this if request.session.has_key('uid'):
    #     return HttpResponse("Logged in...")

def doctor_logout(request):
    try:
        del request.session['uid']
        return redirect('/doctor/loginpage')
    except:
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")
#Patients List 
def patientList(request):
    data = Patient.objects.all()
    return render(request, "patientlist.html", {'data':data})   

