Innovative Healthcare
Patient prescription creation and storing medical history using Postgresql, Django and Bootstrap
Github: https://github.com/Its-Puja-Singh/HackathonBackend
Prerequisites
1. Install Python3 and Django and postgres
2. Any Editor (Preferably VS Code or Sublime Text)
3. Any web browser with latest version
Languages and Technologies used
1. HTML5/CSS3
2. JavaScript (to create dynamically updating content)
3. Bootstrap (An HTML, CSS, and JS library)Php
4. PostgreSQL (An RDBMS that uses SQL)
5. Python and Django
Steps to run the project in your machine
1. Clone or download the repository.
2. Create a database named hackfest in postgresql.
3. Make migrations using the following command:
python manage.py makemigrations 
python manage.py migrate


4. The accounts_role table is being used as master table so enter data in the same 
using:
INSERT INTO table_name (role)
VALUES
    (‘Doctor’),
    (‘Nurse’),
    (‘Admin’);
5. Then run “python manage.py createsuperuser” to create an admin or superuser.
And then inside the accounts_userrolemap insert data for the admin you created:
INSERT INTO accounts_userrolemap  (user_id,role_id)
VALUES
    (1,3);
6. Run “python manage.py runserver” to run the server on localhost.


GETTING INTO THE PROJECT:
This system has a ‘Home’ page which has two main goal:
1. Sign in: To Sign in
2. Prescription: To view prescriptions by patient using registration Id.
3. About Us
  

'About Us' page  allows us to get some more information about the quality and the services of the hospital.
  

A user can Sign in as:
1. Admin
2. Doctor 
3. Nurse
  

After clicking on Prescription, the below page will be rendered where patients can fill their registration numbers sent to them via registered email.
  

Admin Role:
Here admin will have two options:
1. Create Nurse
2. Create Doctor
  

Nurse Role:
They will have two options unlike a doctor:
1.  View Patients and 
2. Register Patients
  



On view patients, a list of patients will be rendered and there are two options:
1. View records: On this page, they can view the patient data but can’t add Prescription.
  

After clicking on view records:
  

Inside the Medical History tab, by clicking on the update button they can update the details of a patient.
  

Inside the Prescriptions tab, by clicking on view diagnosis they can view the details or by clicking on downloads, they can download the e prescription.
  

Inside the Diagnosis details tab:
  

Inside the medical device details tab:
  

Inside the tests tab:
  

Inside the medicine tab, where they can click on the view button to view the medicine details.
  

From the Nurse Home page, they they can choose to register a new patient by clicking Register Patient:
  

When registrations is successfully, a success message will be displayed with an option to add his medical detail:
  

Add Patient Details Page:
  



Doctor Role:
Doctor can view patient list:
  

Unlike Nurse, doctors can Add Prescriptions:
  



Here, he can view the details and click on Add Prescriptions to create new prescriptions.
He can fill the form for diagnosis details and medical device details.
  





After adding prescription and clicking on view diagnosis, they can add medicine and add tests.
  





class Medicine(models.Model):
    name 
    form    
    category 
    strength     
    concentration 
    unitOfPreparation 
    manufacturer 
    expiryDate 
    amount 
    role 
    description 


class Diagnosis(models.Model):
    diagnosisName 
    diagnosisBodySite     
    dateOfOnset 
    severity 
    dateOfAbatement 
    diagnosisCertainity
    diagnosisDescription  
    createdDate  


class MedicalDevice(models.Model):
    deviceName 
    deviceBodySite 
    deviceUse 
    deviceDscription 


class LaboratoryTest(models.Model):
    testName 
    testSpecimen 
    testBodySite 
    testUse 
    testDescription 


class LabTestPrescriptionMap(models.Model):
    laboratoryTestId     
    prescriptionId 


class Prescription(models.Model):
    patientId 
    diagnosisId 
    medicalDevice 


class MedicineDirection(models.Model):
    medicineId 
    doseUnit
    duration     
    doseTiming 
    additionalInstruction 
    reason 


class MedicineDirPrescriptionMap(models.Model):
    prescriptionId     
    medicineDirectionId