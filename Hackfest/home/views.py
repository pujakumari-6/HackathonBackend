from django.shortcuts import redirect, render
from healthcare.models import Patient

# Create your views here.
def homePage(request):
    return render(request, 'homePage.html', {})
def aboutUs(request):
    return render(request, 'about.html', {})
def registrationNo(request):
    return render(request, 'registrationNo.html', {})
def registrationNoSubmit(request):
    registrationNumber = request.POST['registerId']
    patient = Patient.objects.filter(registrationNumber=registrationNumber).first()
    patientId=patient.id
    return redirect('diagnosis',patientId)
    