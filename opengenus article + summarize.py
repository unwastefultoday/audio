#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re

# Make HTTP request to the URL
url = 'https://iq.opengenus.org/association-in-unsupervised-learning/'
response = requests.get(url)

# Parse HTML using BeautifulSoup and lxml
soup = BeautifulSoup(response.content, 'lxml')

# Remove unwanted elements such as code, tables, sidebar, etc.
for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
    elem.extract()

# Extract text from the remaining elements
text = soup.get_text()


# Remove extra whitespace and newlines
text = ''.join(text).strip()

# Print the extracted text
print(text)


# In[2]:


with open('association in unsupervised learning.txt', 'w') as f:
    for word in text:
        try:
            f.write(word)
        except:
            f.write('abc')


# In[3]:


from gtts import gTTS
import os
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save("association in unsupervised learning.mp3")
os.system("mpg321 hello.mp3")


# In[4]:


with open ("association cleaned.txt", "r") as myfile:
    data = myfile.read()
print(data)


# In[5]:


topic_name = soup.find('h1',class_='post-full-title').text
intro_text = f'Today we will learn about {topic_name}. '
outro_text=f'This was all about {topic_name} . For code files and additional information, please visit www.iq.opengenus.org/'


# In[6]:


data = intro_text+'\n'+data+'\n'+outro_text
print(data)


# In[7]:


from gtts import gTTS
import os
language = 'en'
speech = gTTS(text=data, lang=language, slow=False)
speech.save("association cleaned.mp3")
os.system("mpg321 hello.mp3")


# In[8]:


get_ipython().system('pip install sumy')


# In[9]:


# Load Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Creating text parser using tokenization
parser = PlaintextParser.from_string(data, Tokenizer("english"))

from sumy.summarizers.text_rank import TextRankSummarizer

# Summarize using sumy TextRank
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, 10)

text_summary = ""
for sentence in summary:
  text_summary += str(sentence)

print(text_summary)


# In[10]:


from gtts import gTTS
import os
language = 'en'
speech = gTTS(text=text_summary, lang=language, slow=False)
speech.save("association cleaned summarised.mp3")
os.system("mpg321 hello.mp3")


# In[ ]:




