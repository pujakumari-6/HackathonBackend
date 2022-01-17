from django.shortcuts import redirect, render,HttpResponse
from healthcare.models import Patient


# Create your views here.
def homePage(request):
    try:
        return render(request, 'homePage.html', {})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")    
def aboutUs(request):
    try:
        return render(request, 'about.html', {})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")       
def registrationNo(request):
    try:
        return render(request, 'registrationNo.html', {})
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")        
def registrationNoSubmit(request):
    try:
        registrationNumber = request.POST['registerId']
        patient = Patient.objects.filter(registrationNumber=registrationNumber).first()
        patientId=patient.id
        return redirect('diagnosis',patientId)
    except Exception as e:
        print(e)
        return HttpResponse("<h1>something went wrong!!!</h1>")        
    