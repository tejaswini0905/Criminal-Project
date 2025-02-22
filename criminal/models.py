from django.db import models


class Criminal(models.Model):
    Case_Id = models.CharField(max_length=255)
    Registration_Date = models.CharField(max_length=255)
    Date_of_Incident = models.CharField(max_length=255)
    Natureof_Case = models.CharField(max_length=255)
    Incident_address = models.CharField(max_length=255)
    Case_Incharge = models.CharField(max_length=255)

    # abc = models.CharField(max_length=255,default=None)


class PoliceRecords(models.Model):
    Officer_ID = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Date_of_Birth = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Officer_email = models.CharField(max_length=255)
    MObile_no = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    cphoto = models.ImageField(upload_to="images")


class CriminalRecords(models.Model):
    Criminal_Name = models.CharField(max_length=255)
    Alias = models.CharField(max_length=255)
    DOB = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Height = models.CharField(max_length=255)
    Weight = models.CharField(max_length=255)
    Hair_Colour = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to="media", default=None)
    # photo = models.ImageField(upload_to='images/', blank=True, null=True)
    photo = models.ImageField(upload_to="images")
    cateogary = models.CharField(max_length=255)
    Case_Incharge = models.CharField(max_length=255)


class FIR_Records(models.Model):
    PoliceStation_Name = models.CharField(max_length=255)
    Name_of_Accused = models.CharField(max_length=255)
    Type_of_Incident = models.CharField(max_length=255)
    Date_of_complaint = models.CharField(max_length=255)
    Applicant_Name = models.CharField(max_length=255)
    Applicant_LastName = models.CharField(max_length=255)
    Address_Street = models.CharField(max_length=255)
    Address_City = models.CharField(max_length=255)
    Date_of_reported_incident = models.CharField(max_length=255)
    Incident_Location = models.CharField(max_length=255)
    Relation_with_AccusedPerson = models.CharField(max_length=255)

