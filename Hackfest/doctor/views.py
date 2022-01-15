from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from .models import Prescription, PrescribedMedicine, Medicine
from healthcare.models import Patient, PatientRecord

def doctorHome(request):
    return render(request, "doctor.html", {})   

# Patient List
def patientList(request):
    data = Patient.objects.all()
    return render(request, "patientlist.html", {'data':data})   

# Patient Detail
def patientRecord(request, id):
    history = PatientRecord.objects.filter(id=id)
    details = Patient.objects.filter(pk=id).first()
    if(len(history) !=0):
        patientHistory = history.first()
        return render(request, "patientrecord.html", {'history':patientHistory, 'details':details}) 
    else:
        return render(request, "patientrecord.html", {'history':'', 'details':details})

#def doctorLogin(request):
    #return render(request, "doctor.html")  
# Adding Prescription
def makeprescriptions(request):
    if request.method == 'POST':
        patientId = request.session.get('id')
        patient = Patient.objects.get(patientId=patientId)
        prescriptionsDate = request.POST["date"]
        priscription = Prescription(prescriptionIssueDate=prescriptionsDate,prescriptionPatient=patient)
        priscription.save()
        return render(request, "",{"data":priscription})

# Add medcine on Prescription
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
    return render(request, 'addprescription.html')    


# See Prescription
def seePrescription(request):
    patientId = request.session.get('id')
    return render(request, "Patient/patient_prescription.html")

