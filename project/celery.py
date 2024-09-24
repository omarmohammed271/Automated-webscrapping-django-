from __future__ import absolute_import, unicode_literals  
import os  
from celery import Celery  
from django.conf import settings 
from etmad.tasks import scrape_data_task 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
app = Celery('myproject')  
app.config_from_object('django.conf:settings', namespace='CELERY')  
app.autodiscover_tasks()  

# Define periodic tasks  
from celery.schedules import crontab  

@app.on_after_configure.connect  
def setup_periodic_tasks(sender, **kwargs):  
    sender.add_periodic_task(crontab(hour='*', minute=0), scrape_data_task.s())