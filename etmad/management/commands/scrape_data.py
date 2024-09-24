import os  
import django  
import requests  
from requests_html import HTMLSession  
from django.core.management.base import BaseCommand  
from etmad.models import Tender  

# Set up Django environment  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
django.setup()  

class Command(BaseCommand):  
    help = 'Scrape data from a website'  

    def handle(self, *args, **kwargs):  
        session = HTMLSession()  
        for i in range(1,50):
        # URL of the page you want to scrape  
            url = f'https://tenders.etimad.sa/Tender/AllTendersForVisitor?PageNumber={i}'  

            # Send a GET request to the URL  
            response = session.get(url)  
            response.html.render(timeout=30)
            print(response)


            # Select the elements you want to scrape  
            tender_cards = response.html.find('div.tender-card')  
            # print(tender_cards)
            
                # Loop through the tender cards and extract data  
            for card in tender_cards:  
                # Extract the reference number  
                ref_number = card.attrs.get('data-ref')  
                
                # Extract the tender title  
                title_element = card.find('h3 a', first=True)  
                title = title_element.text if title_element else 'No title found'  
                # Extract the price  
                price_element = card.find('div.text-center.mb-3 span', first=True)  
                price = price_element.text if price_element else 'No price found'  

                # Extract the date  
                date_element = card.find('span[title]', first=True)  
                date = date_element.text.strip() if date_element else 'No date found'
                # Extract the dateline  
                date_element_line = card.find('span.ml-3', first=True)  
                dateline = date_element_line.text.strip() if date_element else 'No date found'
                
                # Extract the link  
                link = title_element.attrs.get('href') if title_element else 'No link found'  
                new_link = 'https://tenders.etimad.sa'+link

                Tender.objects.update_or_create(
                    ref_number=ref_number,title=title,price=price,
                    date = date,dateline=dateline
                )
                
                
                print('Done Tender')
                print('---------------------')
        print(f'page: {i} was done')          

        # Close the session  
        session.close()