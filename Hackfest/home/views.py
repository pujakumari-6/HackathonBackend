from django.shortcuts import redirect, render,HttpResponse
from healthcare.models import Patient


# Create your views here.
def homePage(request):
    try:
        return render(request, 'home.html', {})
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
    # try:
        registrationNumber = request.POST['registerId']
        patient = Patient.objects.filter(registrationNumber=registrationNumber)
        if(patient.exists()):
            patientId=patient.first().id
            return redirect('patientDiagnosis',patientId)
        else:
            return HttpResponse("<h1>No records found!!</h1>")     
    # except Exception as e:
    #     print(e)
    #     return HttpResponse("<h1>something went wrong!!!</h1>")        
    