import os  
import django  
# Set up Django environment  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
django.setup()  

from etmad.models import Tender 

def remove():
    tenders = Tender.objects.all()
    
    for i in tenders:
        i.delete()

    print('Done') 

remove()