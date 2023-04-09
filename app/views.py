from django.shortcuts import render
from app.models import *
# Create your views here.
def display_dept(request):
    LOD=DEPT.objects.all()
    d={'dept':LOD}
    return render(request,'display_dept.html',d)

def display_emp(request):
    LOE=EMP.objects.all()
    d={'emp':LOE}
    return render(request,'display_emp.html',d)