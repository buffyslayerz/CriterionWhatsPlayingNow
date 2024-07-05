import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def get_elements(site, classes):
    response = requests.get(site)
    if response.status_code == 200:
        bs = BeautifulSoup(response.content, 'html.parser')
        elements = bs.select(classes)
        if elements:
            texts = [element.get_text().strip() for element in elements]
            return texts[1:3]  

site = 'https://whatsonnow.criterionchannel.com'
classes = '.whatson__title, .whatson__eyebrow--bold'  
elements_text = get_elements(site, classes)

if isinstance(elements_text, list) and len(elements_text) == 2:
    movie, length_left = elements_text  
    match = re.search(r'(\d+)\s+minutes', length_left)
    if match:
        left_minutes = int(match.group(1))
        current_time = datetime.now()
        new_time = current_time + timedelta(minutes=left_minutes)
        timezone = datetime.now().astimezone().tzinfo
        print(movie)
        print(length_left)
        print(new_time.strftime('%H:%M'), timezone)
