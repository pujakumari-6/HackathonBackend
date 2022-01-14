import json
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
import random
from healthcare.models import Patient, PatientRecord
from django.core.mail import send_mail
import uuid
# Create your views here.
def patientRecord(request):
    # if request.session.has_key('uid'):
            if request.method == 'POST':
                try:
                    name = request.POST['name']
                    mobile = request.POST['mobile']
                    email = request.POST['email']
                    gender = request.POST['gender']
                    dateOfBirth = request.POST['dateOfBirth']
                    bloodGroup = request.POST['bloodGroup']
                    uuidNo = str(uuid.uuid4()).replace("-","")[0:10]
                    registrationNumber = name.replace(' ','')+uuidNo+str(random.randint(2345678909800, 9923456789000))[0:5]
                    patientData = Patient()
                    patientData.email = email
                    patientData.name = name
                    patientData.mobile = mobile
                    patientData.gender = gender
                    patientData.dateOfBirth = dateOfBirth
                    patientData.bloodGroup = bloodGroup
                    patientData.registrationNumber = registrationNumber
                    patientData.save()
                except:
                    return render(request, 'newPatient.html',{'message':'Something went Wrong'})
                try:
                    send_mail(
                        subject='Registered to Innovative Healthcare',
                        message='',
                        html_message=f'''Hi {name}, <br><br>
                    Thank you for being part of Innovative healthcare.<br> Use the following registration id to view you prescription history<br><br>
                    {registrationNumber}<br>
                    Team PSCSocial''',
                        from_email='Innovative Healthcare',
                        recipient_list=[email]
                    )
                except Exception as e:
                    print(e)
                    return render(request, 'newPatient.html',{'message':'Failed To Send Email'})
                finally:
                    return render(request, 'newPatient.html',{'success':True})
                
            else:
                return render(request, 'newPatient.html')
    # else:
    #         return redirect('/')



