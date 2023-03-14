from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import UploadHistory
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from django.conf import settings
from django.template.response import TemplateResponse

# Create your views here.
def conv_app(request):
    upload_history = UploadHistory.objects.all().values()
    context = {'upload_history': upload_history}
    
    if request.method == 'POST':

        csv_file = request.FILES['filefield']
        out_format = request.POST.get('outputformat')
        # filename = csv_file.name[:-4]
        filename = str(csv_file.name).split(".")[0]

        # to store file type
        if out_format == settings.XLS_FORMAT:
            type = "xls"
        elif out_format == settings.XLSX_FORMAT:
            type = "xlsx"

        UploadHistory.objects.create(file_name=filename,converted_type=type)

        try:

            df = pd.read_csv(csv_file)
        
            # xlsX
            if out_format == '1':
                # openpyxl set workbook and activate it
                wb = Workbook()
                winit = wb.active

                # get rows from csv and append to xlsx
                for row in dataframe_to_rows(df,index=False,header=True):
                    winit.append(row)
                
                # to download
                response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={filename}_converted.xlsx'
                
                return response
            
            # xls
            elif out_format == '2':
                 # openpyxl set workbook and activate it
                wb = Workbook()
                winit = wb.active
                
                # get rows from csv and append to xls
                for rows in dataframe_to_rows(df,index=False,header=True):
                    winit.append(rows)
                
                # to download
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = f'attachment; filename={filename}_converted.xls'
                # upload_history = UploadHistory.objects.all().values()
                # context = {'upload_history': upload_history}

                # response = TemplateResponse(request, 'app_converter.html', context)

                # return render(request , 'app_converter.html', context)
                return response    


            
        except Exception as e:
            print(e)
            

    return render(request , 'app_converter.html', context)

def delete(request):
    UploadHistory.objects.all().delete()
    return redirect('/')

def refresh(request):
    return redirect('/')