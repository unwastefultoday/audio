#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
from gtts import gTTS
import os

# Make HTTP request to the URL
url = 'https://iq.opengenus.org/association-in-unsupervised-learning/'
response = requests.get(url)

# Parse HTML using BeautifulSoup and lxml
soup = BeautifulSoup(response.content, 'lxml')

# Remove unwanted elements such as code, tables, sidebar, etc.
for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
    elem.extract()

# Extract text from the remaining elements
text = soup.get_text()
# Remove extra whitespace and newlines
text = ''.join(text)
# Print the extracted text
print(text)

#save text
with open('association in unsupervised learning.txt', 'w') as f:
    for word in text:
        try:
            f.write(word)
        except:
            f.write('abc')


# audio conversion
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save("association in unsupervised learning.mp3")
os.system("mpg321 hello.mp3")





