from django.shortcuts import render
import xlsxwriter
from io import BytesIO
from datetime import datetime
from django.http import Http404, HttpResponse
from myapp import models
import codecs

# Create your views here.

def exportexcel(request):


    if 'export' in request.POST:
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('name1')

        format = workbook.add_format()
        format.set_font_size(14)
        format.set_font_name('Arial')
        format.set_color('orange')
        format.set_align('center')

        format1 = workbook.add_format()
        format1.set_font_size(14)
        format1.set_font_name('Arial')
        format1.set_bold()

        # sheet heading
        worksheet.write('A1', 'Danh sach', format1)
        worksheet.write('A2', 'site1', format1)
        worksheet.write('A3', 'site2', format1)
        worksheet.write('A4', 'site3', format1)
        worksheet.write('A5', 'site4', format1)
        worksheet.write('B1', 'Dia chi', format)
        worksheet.write('B2', '0.0.0.0', format)
        worksheet.write('B3', '0.0.1.0', format)
        worksheet.write('B4', '0.1.1.0', format)
        worksheet.write('B5', '1.1.1.0', format)

        workbook.close()
        output.seek(0)
        response = HttpResponse(output.read(), content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename = export-file-demo.xlsx'
        return response
    return render(request,'export.html')

def storedView(request):
    if request.method == 'POST' and request.FILES['myfile']:
        enc_base = request.POST.get('enc_base')
        data_en = str(enc_base).replace('<img src="data:image/jpeg;base64,', '').replace(
            '<img src="data:image/png;base64,', '').replace('">', '')

        data = models.Profile(image= data_en)
        data.save()
        # print('hello anh em')
        # print(data)
    return render(request, 'image.html')

def show(request):
    DATA = models.Profile.objects.all()
    print(DATA[0].image)
    return render(request, 'showimage.html', {'data': DATA})
def convertbase64(request):
    hex_string=''
    base64=''
    if 'btnconvert' in request.POST:
        hex_string=request.POST.get('txthex')
        base64=codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode()
    cut_string=''
    if 'btncut' in request.POST:
        string.lstrip()
    return render(request,'convert.html',{'data':base64})

