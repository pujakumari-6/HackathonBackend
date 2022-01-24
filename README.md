# Innovative Healthcare

Patient prescription creation and storing medical history using Postgresql, Django and Bootstrap
Github: https://github.com/Its-Puja-Singh/HackathonBackend

## Prerequisites
* Install Python3 and Django and PostgreSQL
* Any Editor (Preferably VS Code or Sublime Text)
* Any web browser with latest version

## Languages and Technologies used
* HTML5/CSS3
* JavaScript (to create dynamically updating content)
* Bootstrap (An HTML, CSS, and JS library)
* PostgreSQL (An RDBMS that uses SQL)
* Python and Django

## Steps to run the project in your machine
* Clone or download the repository.
* Create a database named hackfest in postgresql.
* Make migrations using the following command:
    * `python manage.py makemigrations`
    * `python manage.py migrate`


* The accounts_role table is being used as master table so enter data in the same using:

```
INSERT INTO table_name (role)
VALUES
    (‘Doctor’),
    (‘Nurse’),
    (‘Admin’);
```
* Then run `python manage.py createsuperuser` to create an admin or superuser.
And then inside the accounts_userrolemap insert data for the admin you created:
```
INSERT INTO accounts_userrolemap  (user_id,role_id)
VALUES
    (1,3);
```
6. Run `python manage.py runserver` to run the server on localhost.


# GETTING INTO THE PROJECT:
This system has a `Home` page which has two main goal:

* Sign in: To Sign in
* Prescription: To view prescriptions by patient using registration Id.
* About Us
  

`About Us` page  allows us to get some more information about the quality and the services of the hospital.
  

## A user can Sign in as:

* Admin
* Doctor 
* Nurse
  

After clicking on Prescription, the below page will be rendered where patients can fill their registration numbers sent to them via registered email.
  

## Admin Role:
Here admin will have two options:
* Create Nurse
* Create Doctor
  

## Nurse Role:
They will have two options unlike a doctor:
*  View Patients and 
* Register Patients
  



### On view patients, a list of patients will be rendered and there are two options:
* View records: 
    * On this page, they can view the patient data but can’t add Prescription.
  

    * After clicking on view records:
  

* Inside the Medical History tab: 
    * By clicking on the update button they can update the details of a patient.
  

* Inside the Prescriptions tab:
    * By clicking on view diagnosis they can view the details or by clicking on downloads, they can download the e prescription.
  

  

* Inside the tests tab:
  

    * Inside the medicine tab, where they can click on the view button to view the medicine details.
  

    * From the Nurse Home page, they they can choose to register a new patient by clicking Register Patient:
  

    * When registrations is successfully, a success message will be displayed with an option to add his medical detail:
  

### Add Patient Details Page:
  



## Doctor Role:
Doctor can view patient list:
  

* Unlike Nurse, doctors can Add Prescriptions:
  



* Here, he can view the details and click on Add Prescriptions to create new prescriptions.
* He can fill the form for diagnosis details and medical device details.
  





* After adding prescription and clicking on view diagnosis, they can add medicine and add tests.
  




```
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
```
```

class Diagnosis(models.Model):
    diagnosisName 
    diagnosisBodySite     
    dateOfOnset 
    severity 
    dateOfAbatement 
    diagnosisCertainity
    diagnosisDescription  
    createdDate  
```
```

class MedicalDevice(models.Model):
    deviceName 
    deviceBodySite 
    deviceUse 
    deviceDscription 
```
```

class LaboratoryTest(models.Model):
    testName 
    testSpecimen 
    testBodySite 
    testUse 
    testDescription 
```
```

class LabTestPrescriptionMap(models.Model):
    laboratoryTestId     
    prescriptionId 

```
```
class Prescription(models.Model):
    patientId 
    diagnosisId 
    medicalDevice 

```
```
class MedicineDirection(models.Model):
    medicineId 
    doseUnit
    duration     
    doseTiming 
    additionalInstruction 
    reason 
```
```
class MedicineDirPrescriptionMap(models.Model):
    prescriptionId     
    medicineDirectionId
```
