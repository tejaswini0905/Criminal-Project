from django.contrib import admin

# Register your models here.
from .models import Criminal,CriminalRecords, PoliceRecords, FIR_Records

admin.site.register(Criminal)
admin.site.register(CriminalRecords)
admin.site.register(PoliceRecords)
admin.site.register(FIR_Records)
