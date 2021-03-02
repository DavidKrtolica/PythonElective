import os
import subprocess

subprocess.run(['pip', 'install', 'requests'])
subprocess.run(['pip3', 'install', 'beautifulsoup4'])

import requests
from bs4 import BeautifulSoup

pageURL = 'https://www.jobindex.dk/jobsoegning?q=python'
page = requests.get(pageURL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='PaidJob-inner')

for job in results:
    title = job.find('b')
    print(title.text.strip())
