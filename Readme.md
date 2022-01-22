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
4. Then run “python manage.py createsuperuser” to create an admin or superuser.
5. Run “python manage.py runserver” to run the server on localhost.


GETTING INTO THE PROJECT:
This system has a ‘Home’ page which has two main goal:
1. Sign in: To Sign in
2. Prescription: To view prescriptions by patient using registration Id.
  

'About Us' page  allows us to get some more information about the quality and the services of the hospital.
  

A user can Sign in as:
1. Admin
2. Doctor 
3. Nurse
  

After clicking on Prescription, the below page will be rendered where patients can fill their registration numbers sent to them via registered email.
  



After clicking on Get Report the following page will be displayed
  

Here all the details will be displayed including his diagnosis list.
He can click on View Diagnosis to view details:
  



Admin Role:
Here admin will have two options:
1. Create Nurse
2. Create Doctor
Doctor Role:
Doctor can view patient list:
  

On the below page, he can click on View Records to view the details of a patient:
  

Here, he can view the details and click on Add Prescriptions to create new prescriptions.
  



He can fill the form for diagnosis details and click on Add Medicine to prescribe medicine.
  



Using the below page, he can add medicine as many number of times as he wants:
  

Nurse Role:
They will have two options unlike a doctor:
1.  View Patients and 
2. Register Patients
  



On view patients, a list of patients will be rendered and there are two options:
1. View records: On this page, they can view the patient data but can’t add Prescription.
2. Update: To update the registered patient’s medical and other relevant details.
  

Update Patient Page:
  

From the Nurse Home page, they shecan choose to register a new patient by clicking Register Patient:
  

When registrations is successfully, a success message will be displayed with an option to add his medical detail:
  

Add Patient Details Page: