import pandas as pd
from django.shortcuts import render


# Create your views here.
def conv_app(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('filefield')
        df_name = 'converted.xls'
        df = pd.read_csv(upload_file)
        newdf = df.to_excel(df_name,index=False)
    
    return render(request , 'convapp.html')