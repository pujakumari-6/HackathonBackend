from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from .models import Prescription, Medicine, Diagnosis,MedicalDevice,LaboratoryTest,MedicineDirection,MedicineDirPrescriptionMap
from healthcare.models import Patient, PatientRecord


def doctorHome(request):
    try:
        if request.session['role']!= "Doctor" and request.session['role']!="Nurse":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})
        return render(request, "doctor.html", {}) 
    except Exception as e:
        print(e)
        return render(request, "index.html", {'message':'Something Went wrong'})

# Patient List
def patientList(request):
    try:
        print(request.session['role'])
        if request.session['role']!= "Doctor" and request.session['role']!="Nurse":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})

        data = Patient.objects.all()
        return render(request, "patientlist.html", {'data':data})     
    except Exception as e:
        print(e)
        return render(request, "viewPatientRecord.html", {'message':'Something went wrong'})

# Patient Detail
def patientRecord(request, patientId):
    try:
        patientDetails = Patient.objects.get(pk=patientId)
        history = PatientRecord.objects.get(patientId=patientId)
        allPrescription = Prescription.objects.filter(patientId=patientDetails)
        prescriptionListData = []
        for prep in allPrescription:
            diagnosis = Diagnosis.objects.get(pk=prep.diagnosisId.id)
            prescriptionListData.append({
                'diagnosisCreatedDate': diagnosis.createdDate,
                'diagnosisName': diagnosis.diagnosisName,
                'prescriptionId':prep.id
            })
        return render(request, "viewPatientRecord.html", {'history':history, 'details':patientDetails,'prescriptionList':prescriptionListData}) 
    except Exception as e:
        print(e)
        return render(request, "viewPatientRecord.html", {'message':'Something went wrong'})
# See Prescription

def viewPrescription(request, prescriptionId):
    try:
        prescription = Prescription.objects.get(pk=prescriptionId)
        patient = Patient.objects.get(pk=prescription.patientId.id)
        diagnosis = Diagnosis.objects.get(pk=prescription.diagnosisId.id)
        medicalDevice = MedicalDevice.objects.get(pk=prescription.medicalDevice.id)
        laboratoryTest = LaboratoryTest.objects.get(pk=prescription.laboratoryTestId.id)
        medicinDirMap = MedicineDirPrescriptionMap.objects.filter(prescriptionId=prescription)
        if len(medicinDirMap) != 0:
            print('in if')
            medsDirList = []
            for entry in medicinDirMap:
                medsDir = MedicineDirection.objects.filter(pk=entry.medicineDirectionId.id).first()
                medsName = Medicine.objects.filter(pk=medsDir.medicineId.id).first()
                medsDirList.append({
                    'medsDir':medsDir,
                    'medsName':medsName
                })
                print(medsDirList)
            data = {
            'patient':patient,
            'diagnosis':diagnosis,
            'medicalDevice':medicalDevice,
            'laboratoryTest':laboratoryTest,
            'medsDirList':medsDirList
            }
            return render(request, "diagnosisDescription.html",{'data':data})
        else:
            data = {
                'patient':patient,
                'diagnosis':diagnosis,
                'medicalDevice':medicalDevice,
                'laboratoryTest':laboratoryTest,
            }
            return render(request, "diagnosisDescription.html",{'data':data})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")   
def diagnosis(request, patientId):
    try:
        if request.session['role']!= "Doctor":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})

        patient = Patient.objects.filter(id=patientId).first()
        if request.method == 'POST':
            diagnosisName = request.POST.get('diagnosisName',None)
            diagnosisBodySite = request.POST.get('diagnosisBodySite',None)
            if request.POST['dateOfOnset'] == '':
                dateOfOnset = None
            else:
                dateOfOnset = request.POST['dateOfOnset']
            severity = request.POST.get('severity',None)
            if request.POST['dateOfAbatement'] == '':
                dateOfAbatement = None
            else:
                dateOfAbatement = request.POST['dateOfAbatement']
            diagnosisCertainity = request.POST.get('diagnosisCertainity',None)
            diagnosisDescription = request.POST.get('diagnosisDescription',None)
            deviceName = request.POST.get('deviceName',None)
            deviceBodySite = request.POST.get('deviceBodySite',None)
            deviceUse = request.POST.get('deviceUse',None)
            deviceDescription = request.POST.get('deviceDescription',None)
            testName = request.POST.get('testName',None)
            testBodySite = request.POST.get('testBodySite',None)
            testUse = request.POST.get('testUse',None)
            testDescription =  request.POST.get('testDescription',None)
            testSpecimen =  request.POST.get('testSpecimen',None)
            diagnosisData = Diagnosis.objects.create(diagnosisName=diagnosisName,diagnosisBodySite=diagnosisBodySite,dateOfOnset=dateOfOnset,severity=severity,dateOfAbatement=dateOfAbatement,diagnosisCertainity=diagnosisCertainity,diagnosisDescription=diagnosisDescription)
            deviceData = MedicalDevice.objects.create(deviceName=deviceName,deviceBodySite=deviceBodySite,deviceUse=deviceUse,deviceDscription=deviceDescription)
            laboratoryTestData = LaboratoryTest.objects.create(testName=testName,testBodySite=testBodySite,testUse=testUse,testDescription=testDescription, testSpecimen=testSpecimen)
            prescriptionData = Prescription.objects.create(patientId=patient,diagnosisId=diagnosisData,medicalDevice=deviceData,laboratoryTestId=laboratoryTestData)
            allMeds = Medicine.objects.all()
            return render(request, "medicationPage.html",{'prescriptionId':prescriptionData.id,'allMeds':allMeds})

        else:
            return render(request, "diagnosisPage.html",{'patient':patient})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")

def medication(request, prescriptionId):
    try:
        if request.session['role']!= "Doctor":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})

        if request.method == 'POST':
            medicineId = request.POST['medicineId']
            medicine = Medicine.objects.filter(id=medicineId).first()
            allMeds = Medicine.objects.all()
            doseUnit = request.POST['doseUnit']
            duration = request.POST['duration']
            doseTiming = request.POST['doseTiming']
            additionalInstruction = request.POST['additionalInstruction']
            reason = request.POST['reason']
            medicationData = MedicineDirection.objects.create(medicineId=medicine,doseUnit=doseUnit,duration=duration,doseTiming=doseTiming,additionalInstruction=additionalInstruction,reason=reason)
            prescription = Prescription.objects.get(pk=prescriptionId)
            medicationDirData = MedicineDirPrescriptionMap.objects.create(prescriptionId=prescription,medicineDirectionId=medicationData)
            return render(request, "medicationPage.html",{'prescriptionId':prescriptionId, 'allMeds':allMeds, 'success':"Medicine Added Successfullty"})
        else:
            return render(request, "medicationPage.html",{'prescriptionId':prescriptionId})
    except Exception as e:
        print(e)
        allMeds = Medicine.objects.all()
        return render(request, "medicationPage.html",{'prescriptionId':prescriptionId,'allMeds':allMeds,'message':"Please Fill All The Required Details!"})
