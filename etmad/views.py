from django.shortcuts import render  
from .models import Tender  

def scraped_data_view(request):  
    data = Tender.objects.all()  
    return render(request, 'etmad/scraped_data.html', {'data': data})