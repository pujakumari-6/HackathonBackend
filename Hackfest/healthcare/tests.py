from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views
from .models import Patient

class npTest(SimpleTestCase):
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('newPatient'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'something went wrong!!!')
        
class prTest(TestCase):
    
    def setUp(self):
        Patient.objects.create(name='John',email="dsafsa@dsfas.co",registrationNumber=12,bloodGroup='a',mobile=23213,gender='m',dateOfBirth="1998-09-02",createdDate="2020-02-01")
    
    def test_text_content(self):
        patient = Patient.objects.get(id=1)
        print(patient.name)
        expected_object_name = f'{patient.name}'
        self.assertEquals(expected_object_name, 'John')
        response = self.client.get(reverse("patientRecord",args=[patient.id]))
        self.assertContains(response, 'something went wrong!!!')
    
    # def test_view_url_by_name(self):
    #     response = self.client.get(reverse('patientRecord/'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, 'something went wrong!!!')
        
class uprTest(SimpleTestCase):
    
    def test_text_content(self):
        response = self.client.get(reverse("updatePatientRecord",args=[1]))
        self.assertContains(response, 'something went wrong!!!')
