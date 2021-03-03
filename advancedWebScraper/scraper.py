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


print('\n\n')

for job in results:
    result = job.find_all('b')
    title = result[0].text.strip()
    company = job.find('p').text.strip()
    print(f'Job title: {title}\nCompany: {company}\n')

print('\n\n')