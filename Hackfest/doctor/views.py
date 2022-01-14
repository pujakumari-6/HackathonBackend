from django.core.checks import messages
from django.shortcuts import redirect, render
<<<<<<< HEAD
from django.http import HttpResponse, response
=======
from django.http import HttpResponse, HttpRequest
from .models import Prescription, PrescribedMedicine, Medicine
from healthcare.models import Patient, PatientRecord
>>>>>>> 5532b48fda7a1870d6b266aa7ac745f18b2ea023
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
        return  render(request, 'ragister.html',{'roleid': 1 } )
    except:
<<<<<<< HEAD
        return HttpResponse("<h1>something went wrong!!!</h1>")
def addDoctor(request):
    try:
        return  render(request, 'ragister.html',{'roleid': 2} )
    except:
        return HttpResponse("<h1>something went wrong!!!</h1>")

=======
        return HttpResponse("<h3>Somthing is wrong !!!!!</h3>")
#Patients List 
def patientList(request):
    data = Patient.objects.all()
    return render(request, "patientlist.html", {'data':data})   
>>>>>>> 5532b48fda7a1870d6b266aa7ac745f18b2ea023

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




<<<<<<< HEAD
=======
def makeprescriptions(request):
    if request.method == 'POST':
        patientId = request.session.get('id')
        patient = Patient.objects.get(patientId=patientId)
        prescriptionsDate = request.POST["date"]
        priscription = Prescription(prescriptionIssueDate=prescriptionsDate,prescriptionPatient=patient)
        priscription.save()
        return render(request, "",{"data":priscription})

def addMedicineOnPrescription(request):
    if request.method=="POST":
        prescribedMedicineDuration=request.POST['prescribedMedicineDuration']
        prescribedMedicineMedicine=request.POST['medicineId']
        prescribedMedicineQuantity=request.POST['prescribedMedicineQuantity']
        prescribedMedicineTakenQuantity=request.POST['prescribedMedicineTakenQuantity']
        prescribedMedicinePrescription=request.POST['prescriptionId']
        prescribedMedicineDiagnosis= request.POST['prescriptionDiagnosis']
        medicine = Medicine.objects.get(medicineId=prescribedMedicineMedicine)
        prescription = Prescription.objects.get(prescriptionId=prescribedMedicinePrescription)

        prescribedMedicine = PrescribedMedicine(prescribedMedicineDuration=prescribedMedicineDuration,prescribedMedicineMedicine=medicine,prescribedMedicineQuantity=prescribedMedicineQuantity,prescribedMedicineTakenQuantity=prescribedMedicineTakenQuantity,prescribedMedicineDiagnosis=prescribedMedicineDiagnosis,prescribedMedicinePrescription=prescription)
        prescribedMedicine.save()
        return HttpResponse("added")

def seePrescription(request):
    patientId = request.session.get('id')
    return render(request, "Patient/patient_prescription.html")


def getPrescriptionsOnId(request):
    if request.method == "GET":
        patientId = request.session.get('id')
        prescriptions = Prescription.objects.raw("select prescriptionId from doctor_prescription inner join healthcare_patient on healthcare_patient.patientId=doctor_prescription.prescriptionPatient where patientId='"+str(patientId)+"'")
        return render(request, "Patient/prescription.html", {"data": prescriptions})


def getPrescriptionMedicineOnId(request):
    if request.method == "GET":
        prescriptionId = request.GET['prescriptionId']
        prescription = Prescription.objects.get(prescriptionId=prescriptionId)
        prescriptionMedicines = PrescribedMedicine.objects.filter(
            prescribedMedicinePrescription=prescription)
        return render(request, "Patient/prescription.html", {"data": prescriptionMedicines})


def addMedicineOnId(request):
    if request.method == "GET":
        medicineId = request.GET['medicineId']
        medicineName=request.POST['medicineName']
        signleUnitQuantity=request.POST['signleUnitQuantity']
        medicine = Medicine(medicineId=medicineId,medicineName=medicineName,signleUnitQuantity=signleUnitQuantity)
        return render(request, "medicine.html", {"data": medicine})


# def getPrescribedMedicineMedicineOnId(request):
#     if request.method == "GET":
#         prescribedMedicineId = request.GET['prescribedMedicineId']
#         prescribedMedicineMedicien = Medicine.objects.filter(
#             prescribedmedicine__prescribedMedicineId=prescribedMedicineId)
#         data = {
#             "prescribedMedicineMedicien": list(prescriptions.values())
#         }
#         return HttpResponse(json.dumps(data))

        
>>>>>>> 5532b48fda7a1870d6b266aa7ac745f18b2ea023
