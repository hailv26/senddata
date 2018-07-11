from django.shortcuts import render
from myapp import models
from datetime import datetime
import codecs
import string
# Create your views here.
def loadhome(request):
    a=[]
    if request.method== "GET":
        xtemp=request.GET.get('temp')
        xhumi=request.GET.get('humi')
        xtime=request.GET.get('time')
        xsensor=request.GET.get('sensor')
        if xtemp and xhumi:
            data=models.Data(temp=xtemp,humi=xhumi,time=xtime,)
            data.save()
    a = models.Data.objects.all()
    return render(request,'home.html',{'a':a})
def plotly(request):
    temp=[]
    time=[]
    humi=[]
    temp=models.Data.objects.all().values_list('temp')
    time=models.Data.objects.all().values_list('time')
    humi=models.Data.objects.all().values_list('humi')
    data=[1,3,5,7,9,11]
    return render(request,'plotly.html',{'data':data,'temp':temp,'time':time,'humi':humi})
def chart(request):
    return render(request,'chart.html')
def convertbase64(request):
    base64=''
    ketqua=''

    if 'btnconvert' in request.POST:
        hex_string=request.POST.get('txthex')
        base64=codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode()
    if 'btncut' in request.POST:
        ketqua=request.POST.get('txtstring')
        cut=request.POST.get('txtcut')
        ketqua=ketqua.replace(cut,'')

    return render(request,'convert.html',{'data':base64,'ketqua':ketqua})

def datahex(request):
    a = []
    if request.method == "GET":
        img = request.GET.get('img')
        if img:

            img=codecs.encode(codecs.decode(img, 'hex'), 'base64').decode()
            data = models.DataHex(img=img,time=request.GET.get('time'),sensor=request.GET.get('sensor'))
            data.save()
    DATA = models.DataHex.objects.all()
    return render(request, 'datahex.html', {'data': DATA})
