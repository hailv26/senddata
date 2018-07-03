from django.shortcuts import render
from myapp import models
# Create your views here.
def loadhome(request):
    a=[]
    if request.method== "GET":
        xtemp=request.GET.get('nhietdo')
        xhumi=request.GET.get('doam')
        data=models.Data(temp=xtemp,humi=xhumi)
        data.save()
    a = models.Data.objects.all()
    return render(request,'home.html',{'a':a})