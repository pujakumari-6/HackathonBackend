from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcare', include('healthcare.urls')),
    path('doctor', include('doctor.urls'))
]
