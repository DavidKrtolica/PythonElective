import os
import subprocess

subprocess.run(['pip', 'install', 'requests'])
subprocess.run(['pip3', 'install', 'beautifulsoup4'])

import requests
from bs4 import BeautifulSoup

inputURL = 'http://www.extremeprogramming.org'
page = requests.get(inputURL)
soup = BeautifulSoup(page.content, 'html.parser')

f = open('xp.html', 'w')
f.write(soup.prettify())

pic1 = requests.get('http://www.extremeprogramming.org/images/xplogo.gif')
pic2 = requests.get('http://www.extremeprogramming.org/images/apo.gif')
pic3 = requests.get('http://www.extremeprogramming.org/images/agileflowchart.gif')
pic4 = requests.get('http://www.extremeprogramming.org/images/xplinkon.gif')

os.mkdir('images')

o = open('images/xplogo.gif', 'wb')
o.write(pic1.content)

p = open('images/apo.gif', 'wb')
p.write(pic2.content)

q = open('images/agileflowchart.gif', 'wb')
q.write(pic3.content)

r = open('images/xplinkon.gif', 'wb')
r.write(pic4.content)