from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from criminal.models import Criminal, FIR_Records, PoliceRecords
from .models import CriminalRecords



# Create your views here.

def first(request):
    return render(request, 'Firstpage.html')
def index(request):
    return render(request, 'index.html')

def adminLogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/Header")

        else:
            # No backend authenticated the credentials
            return render(request, 'adminLogin.html')
    return render(request,'adminLogin.html')

def header(request):
    return render(request, 'header.html')

def back1(request):
    return render(request, 'index.html')


def AddCase(request):
    if request.method == "POST":
        caseid = str(request.POST.get('case_ID'))
        regdate = str(request.POST.get('Regdate'))
        doi = str(request.POST.get('dateofincident'))
        noc = str(request.POST.get('natureOfCase'))
        IncAdd = str(request.POST.get('subject'))
        CaseInc = str(request.POST.get('caseincharge'))

        info = Criminal(Case_Id=caseid,Registration_Date=regdate,Date_of_Incident=doi,Natureof_Case=noc,Incident_address=IncAdd,Case_Incharge=CaseInc)
        info.save()
        messages.success(request, "Case Added Successfully!")
    return render(request, 'AddCaseDetails.html')

def AddOfficer(request):
    if request.method == "POST":
        officerid = str(request.POST.get('officer_ID'))
        officername = str(request.POST.get('officerName'))
        dob = str(request.POST.get('dateofbirth'))
        gen = str(request.POST.get('gender'))
        Email = str(request.POST.get('email'))
        mob = str(request.POST.get('mno'))
        address = str(request.POST.get('off_add'))
        Photoo = request.FILES['imagee']
        info = PoliceRecords(Officer_ID=officerid, Name=officername, Date_of_Birth=dob, Gender=gen,
                        Officer_email=Email, MObile_no=mob,  Address=address, cphoto=Photoo)
        info.save()
        messages.success(request, "Officer Added Successfully!")
    return render(request, 'AddOfficer.html')


def CriminalRecord(request):

    if request.method == "POST":
        ccname = str(request.POST.get('cname'))
        asname = str(request.POST.get('ass'))
        dateob = str(request.POST.get('dob'))
        cage = str(request.POST.get('age'))
        cgender = str(request.POST.get('gender'))
        cheight = str(request.POST.get('h'))
        cwght = str(request.POST.get('wght'))
        cclor = str(request.POST.get('hclr'))
        Photo = request.FILES['image']
        crime = str(request.POST.get('crime'))
        case_Incharge = str(request.POST.get('cin'))


        info = CriminalRecords(Criminal_Name=ccname, Alias=asname, DOB=dateob, Age=cage,
                        Gender=cgender, Height=cheight, Weight=cwght, Hair_Colour=cclor, photo=Photo,cateogary=crime,
                        Case_Incharge=case_Incharge)

        info.save()
        messages.success(request, "Criminal Record Added Successfully!")

    return render(request, 'criminalRecords.html')

def AboutUs(request):
    return render(request, 'aboutus.html')

def SearchCase(request):
    if request.method=="POST":
        cat = request.POST.get("natureOfCase")
        info = CriminalRecords.objects.filter(cateogary=cat)
        pht = info.values('photo')
        contexts={
            "results":info.values(),
        }
        return render(request, 'searchCase.html',contexts)
    else:
        return render(request, 'searchCase.html')

def search(request):

    cateogary = request.cateogary()

    obj = CriminalRecords.all(cateogary=cateogary)

    return obj



def search_data(request):
    if request.method == 'POST':
        entered_value = request.POST.get('entered_value')  # Get the entered value from the submitted form
        results = CriminalRecords.objects.filter(column_name=entered_value)
        return render(request, 'searchCase.html', {'results': results})
    else:
        return render(request, 'searchCase.html')


def AddFIR(request):
    if request.method == "POST":
        PSName = str(request.POST.get('name'))
        AccusedName = str(request.POST.get('aname'))
        tofincident = str(request.POST.get('typeOfIncident'))
        docomplaint = str(request.POST.get('doc'))
        appName = str(request.POST.get('applicantName'))
        appLName = str(request.POST.get('applicantLastName'))
        street = str(request.POST.get('sadd'))
        cityName = str(request.POST.get('city'))
        doReportedIncident = str(request.POST.get('dfri'))
        IncidentLocation = str(request.POST.get('inLocation'))
        Relation = str(request.POST.get('relation'))

        info = FIR_Records(PoliceStation_Name=PSName, Name_of_Accused=AccusedName, Type_of_Incident=tofincident,
                           Date_of_complaint=docomplaint, Applicant_Name=appName, Applicant_LastName=appLName,
                           Address_Street=street, Address_City=cityName,  Date_of_reported_incident=doReportedIncident,
                        Incident_Location=IncidentLocation, Relation_with_AccusedPerson=Relation)
        info.save()
        messages.success(request, "FIR Added Successfully!")
    return render(request, 'fir.html')



def delete(request,id):
    if request.method == 'GET':
      data = CriminalRecords.objects.get(id=id)
      data.delete()
      messages.info(request, "Deleted Successfully!")
    return redirect('/searchcase')


# def FIR_RECORDS(request):
#     if request.method=="POST":
#         info = FIR_Records.objects.all()
#         contexts={
#             "results":info.values()
#         }
#         return render(request, 'firRecords.html',contexts)
#     else:
#         return render(request, 'firRecords.html')


def fir_records(request):
    info = FIR_Records.objects.all()
    contexts = {
        "results": info.values()
    }
    return render(request, 'firRecords.html', contexts)

def officer_records(request):
    info = PoliceRecords.objects.all()
    contexts = {
        "results": info.values()
    }
    return render(request, 'officerRecord.html', contexts)



def fir_record_view(request,ID):
    if request.method == 'GET':
      data = FIR_Records.objects.filter(id=ID).values()[0]
      print(data)
      contexts={
          "policeStationName":data["PoliceStation_Name"],
          "nameOfAccused":data["Name_of_Accused"],
          "typeOfAccident":data["Type_of_Incident"],
          "dateOfConplain":data["Date_of_complaint"],
          "applicantName":data["Applicant_Name"],
          "applicantLastName":data["Applicant_LastName"],
          "addressStreet":data["Address_Street"],
          "addressCity":data["Address_City"],
          "dateOfReportedAccident": data["Date_of_reported_incident"],
          "incidentLocation":data["Incident_Location"],
          "relationWithAccusedPerson":data["Relation_with_AccusedPerson"]
      }
    return render(request,'fir.html', contexts)


def Back(request):
    return render(request, 'header.html')


def editCriminal(request, ID):
    data = CriminalRecords.objects.filter(id=ID).values()[0]
    print(data)
    contexts = {
        "id": ID,
        "Criminal_Name": data["Criminal_Name"],
        "Alias": data["Alias"],
        "DOB": data["DOB"],
        "Age": data["Age"],
        "Gender": data["Gender"],
        "Height": data["Height"],
        "Weight": data["Weight"],
        "Hair_Colour": data["Hair_Colour"],
        "photo": data["photo"],
        "cateogary": data["cateogary"],
        "Case_Incharge": data["Case_Incharge"]}
    return render(request, 'editcriminalRecords.html', contexts)


def edit(request,ID):
    if request.method == 'POST':
      ccname = str(request.POST.get('cname'))
      asname = str(request.POST.get('ass'))
      dateob = str(request.POST.get('dob'))
      cage = str(request.POST.get('age'))
    #   cgender = str(request.POST.get('gender'))
      cheight = str(request.POST.get('h'))
      cwght = str(request.POST.get('wght'))
      cclor = str(request.POST.get('hclr'))
      # Photo = request.POST.get('image')
    #   Photo = request.FILES['image']
    #   crime = str(request.POST.get('crime'))
      case_Incharge = str(request.POST.get('cin'))

      data = CriminalRecords.objects.filter(id=ID)[0]
      data.Criminal_Name=ccname
      data.Alias=asname
      data.DOB=dateob
      data.Age=cage
      data.Height=cheight
      data.Weight=cwght
      data.Hair_Colour=cclor
      data.Case_Incharge=case_Incharge
      data.save()
      return redirect("/searchcase/")
    return render(request,"editcriminalRecords.html")








