from django.shortcuts import render  
from .models import ScrapedData  

def scraped_data_view(request):  
    data = ScrapedData.objects.all()  
    return render(request, 'etmad/scraped_data.html', {'data': data})