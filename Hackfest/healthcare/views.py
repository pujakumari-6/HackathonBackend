from datetime import datetime
import json
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
import random
from healthcare.models import Patient, PatientRecord
from django.core.mail import send_mail
import uuid
from django.conf import settings
# Create your views here.

# register patient



def newPatient(request):
    try:
        if request.session['role']!="Nurse":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})

        if request.method == 'POST':
            try:
                name = request.POST['name']
                mobile = request.POST['mobile']
                email = request.POST['email']
                patient = Patient.objects.filter(email=email)
                if len(patient) != 0:
                    return render(request, 'newPatient.html',{'message':'Patient already exists'})
                gender = request.POST['gender']
                dateOfBirth = request.POST['dateOfBirth']
                bloodGroup = request.POST['bloodGroup']
                uuidNo = str(uuid.uuid4()).replace("-","")[0:10]
                registrationNumber = name.replace(' ','')+uuidNo+str(random.randint(2345678909800, 9923456789000))[0:5]
                patientData = Patient.objects.create(name=name,mobile=mobile,email=email,gender=gender,dateOfBirth=dateOfBirth,bloodGroup=bloodGroup,registrationNumber=registrationNumber)
                patientData.save()
            except:
                return render(request, 'newPatient.html',{'message':'Something went Wrong'})
            try:
                send_mail(
                    subject='Registered to Innovative Healthcare',
                    message='',
                    html_message=f'''Hi {name}, <br><br>
                Thank you for being part of Innovative healthcare.<br> Use the following registration id to view you prescription history<br>
                <b>{registrationNumber}</b><br><br>Regards<br>
                Innovative Healthcare''',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )
            except Exception as e:
                print(e)
                return render(request, 'newPatient.html',{'message':'Failed To Send Email'})
            finally:
                return render(request, 'newPatient.html',{'success':True, 'patientId':patientData.id})
        else:
                return render(request, 'newPatient.html')
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")

# Create new patient record
def patientRecord(request, patientId):
    try:
        if request.session['role']!="Nurse" :
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})

        patient = Patient.objects.filter(id=patientId).first()
        if request.method == 'POST':
                patientRecord = PatientRecord.objects.filter(patientId=patientId)
                if len(patientRecord) != 0:
                    return render(request, 'patientRecord.html',{'message':'Patient record already exists'})
                height = request.POST['height']
                weight = request.POST['weight']
                allergies = request.POST['allergies']
                pregnancyStatus = request.POST.get('pregnancyStatus', None)
                if request.POST.get('estimatedDelivery', None) == None:
                    estimatedDelivery = None
                else:
                    estimatedDelivery = request.POST.get('estimatedDelivery', None)
                bloodPressure = request.POST['bloodPressure']
                pulseRate = request.POST['pulseRate']
                bodyTemprature = request.POST['bodyTemprature']
                isAlcolohic = request.POST.get('isAlcolohic',None)
                isSmoker = request.POST.get('isSmoker',None)
                isDiabetic = request.POST.get('isDiabetic',None)
                insurancePlanName = request.POST['insurancePlanName']
                insurancePlanNumber = request.POST['insurancePlanNumber']
                previousSurgery = request.POST['previousSurgery']
                status = request.POST['status']
                patientRecord = PatientRecord()
                patientRecord.patientId = patient
                patientRecord.bloodPressure =bloodPressure
                patientRecord.pulseRate = pulseRate
                patientRecord.bodyTemprature = bodyTemprature
                patientRecord.isAlcolohic = isAlcolohic
                patientRecord.isSmoker = isSmoker
                patientRecord.height = height
                patientRecord.weight = weight
                patientRecord.allergies = allergies
                patientRecord.pregnancyStatus = pregnancyStatus
                patientRecord.estimatedDelivery = estimatedDelivery
                patientRecord.insurancePlanName = insurancePlanName
                patientRecord.insurancePlanNumber = insurancePlanNumber
                patientRecord.isDiabetic = isDiabetic
                patientRecord.previousSurgery = previousSurgery
                patientRecord.status = status
                patientRecord.save()
                return redirect('/doctor/patient-list')
        else:
            return render(request, 'patientRecord.html', {'patient':patient,'patientId':patientId})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")
        
# update patient record
def updatePatientRecord(request, patientId):
    try:
        if request.session['role']!="Nurse":
            return render(request, 'index.html', {'messages': "You Are Not Authenticated"})

        patientP = Patient.objects.filter(id=patientId).first()
        patient = PatientRecord.objects.filter(patientId=patientId)
        if len(patient) == 0:
            return render(request, 'patientRecord.html',{'message':'Patient desnot exist!'})
        patientRecord = patient.first()
        if request.method == 'POST':
                height = request.POST['height']
                weight = request.POST['weight']
                allergies = request.POST['allergies']
                pregnancyStatus = request.POST.get('pregnancyStatus', None)
                if request.POST.get('estimatedDelivery', None) == None:
                    estimatedDelivery = None
                else:
                    estimatedDelivery = request.POST.get('estimatedDelivery', None)
                bloodPressure = request.POST['bloodPressure']
                pulseRate = request.POST['pulseRate']
                bodyTemprature = request.POST['bodyTemprature']
                isAlcolohic = request.POST.get('isAlcolohic',None)
                isSmoker = request.POST.get('isSmoker',None)
                isDiabetic = request.POST.get('isDiabetic',None)
                insurancePlanName = request.POST['insurancePlanName']
                insurancePlanNumber = request.POST['insurancePlanNumber']
                previousSurgery = request.POST['previousSurgery']
                status = request.POST['status']
                patientRecord.patientId = patientP
                patientRecord.bloodPressure =bloodPressure
                patientRecord.pulseRate = pulseRate
                patientRecord.bodyTemprature = bodyTemprature
                patientRecord.isAlcolohic = isAlcolohic
                patientRecord.isSmoker = isSmoker
                patientRecord.height = height
                patientRecord.weight = weight
                patientRecord.allergies = allergies
                patientRecord.pregnancyStatus = pregnancyStatus
                patientRecord.estimatedDelivery = estimatedDelivery
                patientRecord.insurancePlanName = insurancePlanName
                patientRecord.insurancePlanNumber = insurancePlanNumber
                patientRecord.isDiabetic = isDiabetic
                patientRecord.previousSurgery = previousSurgery
                patientRecord.status = status
                patientRecord.save()

                return render(request, 'updatePatientRecord.html',{'patient':patientRecord,'success':True,'profile':patientP})
                
        else:
            return render(request, 'updatePatientRecord.html', {'patient':patientRecord,'profile':patientP})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")