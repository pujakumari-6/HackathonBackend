from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'homePage.html', {})
def aboutUs(request):
    return render(request, 'about.html', {})
    