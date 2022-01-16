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
    return render(request, "doctor.html", {}) 

# Patient List
def patientList(request):
    data = Patient.objects.all()
    return render(request, "patientlist.html", {'data':data})   

# Patient Detail
def patientRecord(request, patientId):
    # try:
        history = PatientRecord.objects.get(id=patientId)
        patientDetails = Patient.objects.get(pk=patientId)
        allPrescription = Prescription.objects.get(patientId=patientDetails)
        prescriptionListData = []
        for prep in allPrescription:
            diagnosis = Diagnosis.objects.get(id=prep.diagnosisId)
            prescriptionListData.add({
                'diagnosisCreatedDate': diagnosis.createdDate,
                'diagnosisName': diagnosis.diagnosisName,
                'prescriptionId':prep.id
            })
        return render(request, "viewPatientRecord.html", {'history':history, 'details':patientDetails,'prescriptionList':prescriptionListData}) 
    # except Exception as e:
    #     print(e)
    #     return render(request, "viewPatientRecord.html", {'message':'Something went wrong'})
# See Prescription

def viewPrescription(request, prescriptionId):
    prescription = Prescription.objects.get(pk=prescriptionId)
    patient = request.session.get(pk=prescription.patientId)
    diagnosis = Diagnosis.objects.get(pk=prescription.diagnosisId)
    medicalDevice = MedicalDevice.objects.get(pk=prescription.medicalDevice)
    laboratoryTest = LaboratoryTest.objects.get(pk=prescription.laboratoryTestId)
    medicinDirMap = MedicineDirPrescriptionMap.objects.get(prescriptionId=prescription.prescriptionId)
    medsDir = MedicineDirection.objects.get(pk=medicinDirMap.medicineDirectionId)
    medsName = Medicine.objects.get(pk=medsDir.medicineId).name
    data = {
        'patient':patient,
        'diagnosis':diagnosis,
        'medicalDevice':medicalDevice,
        'laboratoryTest':laboratoryTest,
        'medsDir':medsDir,
        'medsName':medsName
    }
    return render(request, "Patient/patientPrescription.html")

def diagnosis(request, patientId):
    patient = Patient.objects.filter(id=patientId).first()
    if request.method == 'POST':
        diagnosisName = request.POST['diagnosisName']
        diagnosisBodySite = request.POST['diagnosisBodySite']
        dateOfOnset = request.POST['dateOfOnset']
        severity = request.POST['severity']
        dateOfAbatement = request.POST['dateOfAbatement']
        diagnosisCertainity = request.POST['diagnosisCertainity']
        diagnosisDescription = request.POST['description']
        deviceName = request.POST['deviceName']
        deviceBodySite = request.POST['bodySite']
        deviceUse = request.POST['deviceUse']
        deviceDescription = request.POST['description']
        testName = request.POST['testName']
        testBodySite = request.POST['testBodySite']
        testUse = request.POST['description']
        testDescription = request.POST['description']
        diagnosisData = Diagnosis.objects.create(diagnosisName=diagnosisName,diagnosisBodySite=diagnosisBodySite,dateOfOnset=dateOfOnset,severity=severity,dateOfAbatement=dateOfAbatement,diagnosisCertainity=diagnosisCertainity,diagnosisDescription=diagnosisDescription)
        deviceData = MedicalDevice.objects.create(deviceName=deviceName,deviceBodySite=deviceBodySite,deviceUse=deviceUse,deviceDescription=deviceDescription)
        laboratoryTestData = LaboratoryTest.objects.create(testName=testName,testBodySite=testBodySite,testUse=testUse,testDescription=testDescription)
        prescriptionData = Prescription.objects.create(patientId=patient,diagnosisId=diagnosisData,medicalDevice=deviceData,laboratoryTestId=laboratoryTestData)
        return render(request, "medicationPage.html",{'prescriptionId':prescriptionData.id})

    else:
        return render(request, "diagnosisPage.html",{'patientId':patientId})


def medication(request, prescriptionId):
    if request.method == 'POST':
        medicineId = request.POST['medicineId']
        medicine = Medicine.objects.filter(id=medicineId).first()
        doseUnit = request.POST['medicineId']
        duration = request.POST['medicineId']
        doseTiming = request.POST['medicineId']
        additionalInstruction = request.POST['medicineId']
        reason = request.POST['medicineId']
        medicationData = MedicineDirection.objects.create(medicineId=medicine,doseUnit=doseUnit,duration=duration,doseTiming=doseTiming,additionalInstruction=additionalInstruction,reason=reason)
        medicationDirData = MedicineDirPrescriptionMap.objects.create(prescriptionId=prescriptionId,medicineDirectionId=medicationData)
        return render(request, "medicationPage.html",{'prescriptionId':prescriptionId})
    else:
        return render(request, "medicationPage.html",{'prescriptionId':prescriptionId})

