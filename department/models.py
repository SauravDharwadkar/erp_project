from django.db import models
from datetime import date


DEPARTMENTS = (
    ('Computer Science','Computer Science'),
    ('Electronics and Telecommunication','Electronics and Telecommunication'),
    ('Mechanical','Mechanical'),
    ('Civil','Civil'),
)
CLASS = (
    ('', 'Choose...'),
    ('SE','SE'),
    ('TE','TE'),
    ('BE','BE'),
)

EXAM_TYPES=(
    ('', 'Choose...'),
    ('MID SEM','MID SEM'),
    ('PRELIMS','PRELIMS'),
    ('END SEM','END SEM'),
)

ENTC_SUB = (
    ('ENTC1','ENTC1'),
    ('ENTC2','ENTC2'),
    ('ENTC3','ENTC3'),
    ('ENTC4','ENTC4'),
    ('ENTC5','ENTC5'),
)

MECH_SUB = (
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
    ('MECH1','MECH1'),
)

CIVIL_SUB = (
    ('C1','C1'),
    ('C2','C2'),
    ('C3','C3'),
    ('C4','C4'),
    ('C5','C5'),
)

COMP_SUB = (
    ('DBMS','DBMS'),
    ('TOC','TOC'),
    ('CN','CN'),
    ('SEMP','SEMP'),
    ('ISEE','ISEE'),
)

SUBJECTS =(
    ('', 'Choose...'),
    (COMP_SUB,COMP_SUB),
    (ENTC_SUB,ENTC_SUB),
    (MECH_SUB,MECH_SUB),
    (CIVIL_SUB,CIVIL_SUB),
)



# Create your models here.

class Department(models.Model):
    department = models.CharField(primary_key=True, max_length=128,unique=True)

    def __str__(self):
        return self.department

class StudentResult(models.Model):
    
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    Class = models.CharField(max_length = 150, choices=CLASS, default='')
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length = 150, choices=EXAM_TYPES, default='')
    subject = models.CharField(max_length = 150, choices=SUBJECTS, default='')
    date = models.DateField(("Date"), default=date.today,auto_now=False, auto_now_add=False)
    appeared = models.IntegerField(null=False, blank=False)
    passed = models.IntegerField(null=False, blank=False)
    perct = models.IntegerField(default=0,null=False, blank=False)
    objects = models.Manager()

class DeptProEvent3(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    activity_name = models.CharField(max_length=150)
    #department_name = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    #department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    resourse_person_name = models.CharField(max_length=150)
    resourse_person_contact = models.IntegerField()
    no_of_participants = models.IntegerField()
    event_from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    event_to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    objects = models.Manager()

    def __str__(self):
        return self.activity_name

class DeptStudPart5(models.Model):
    department = models.CharField(max_length = 150, choices=DEPARTMENTS, default='Computer Science')
    student_name = models.CharField(max_length=150)
    event_type = models.CharField(max_length=150)
    event_name = models.CharField(max_length=150)
    org_inst = models.CharField(max_length=264)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)
    awards = models.CharField(("Recognition Awards"), max_length=264)

#Information about Faculty Development Programs organized by department 
class FacultyDevProOrg_Dep(models.Model):
    program_name = models.CharField(max_length=150)
    department_name = models.CharField(max_length=150)
    sponsoring_agency = models.CharField(max_length=150)
    amm_sponsored = models.IntegerField(default=0)
    from_date = models.DateField(("From"), default=date.today,auto_now=False, auto_now_add=False)
    to_date = models.DateField(("To"), default=date.today,auto_now=False, auto_now_add=False)
    no_of_part = models.IntegerField(("No of Participants"))
    level = models.CharField(max_length=150)



#Start-Up
class StartUp(models.Model):
    startup_name = models.CharField(max_length=150)
    nature_startup = models.CharField(max_length=150)
    date_commencement = models.CharField(max_length=150)
    #TODO ^
    Founder = models.CharField(max_length=150)
    LLP_no = models.IntegerField()
    startup_web = models.CharField(max_length=150)
    team_members = models.CharField( max_length=500)
    #team_member isnt right






# class MY_CHOICES(models.Model)
#     choice = models.CharField(max_length=154, unique=True)

# class MODEL(models.Model):
#     ...
#     ...
#     my_field = models.ManyToManyField(MY_CHOICES)