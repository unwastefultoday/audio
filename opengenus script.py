#!/usr/bin/env python
# coding: utf-8

# In[76]:


def url_to_summarised_audio(input_urls_file,output_file_location):
    from gtts import gTTS
    import requests
    from bs4 import BeautifulSoup
    import re
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    import os
    with open(input_urls_file,'r') as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    for url in urls:
        i=1
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
             elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        topic_name = soup.find('h1',class_='post-full-title')


        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, 10)
        text_summary = ""
        for sentence in summary:
            text_summary += str(sentence)


        intro_text = f'Today we will learn about {topic_name.text} '
        outro_text=f'\nThis was all about {topic_name.text} . For code files and additional information, please visit www.iq.opengenus.org/'
        text_summary = intro_text+'\n'+text_summary+'\n'+outro_text
        with open(topic_name.get_text()+'.txt', 'a') as f:
            for word in text_summary:
                try:
                    f.write(word)
                except:
                    f.write('error'+"\n")

        name=topic_name.get_text()+" summarised.mp3"
        newpath2=output_file_location.split("//")
        newpath=output_file_location.split("//")
        newpath.append(name)
        output_file_location="\\".join(newpath)
        language = 'en'
        speech = gTTS(text=text_summary, lang=language, slow=False)
        speech.save(output_file_location)
        os.system("mpg321 hello.mp3")
        output_file_location="//".join(newpath2)
        print(f"Converted URL {i} to summarised audio")
        i+=1
    print("Converted all URLs to summarised audio")
        
    


# In[77]:


input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
output_file_location="C:\\Users\\Ambarish Deb\\Desktop"
url_to_summarised_audio(input_urls_file,output_file_location)


# In[48]:


def url_to_raw_audio(input_urls_file,output_file_location):
    from gtts import gTTS
    import requests
    from bs4 import BeautifulSoup
    import re
    import os
    with open(input_urls_file,'r') as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    i=1
    for url in urls:
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
             elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        topic_name = soup.find('h1',class_='post-full-title')


        intro_text = f'Today we will learn about {topic_name.text} '
        outro_text=f'\nThis was all about {topic_name.text} . For code files and additional information, please visit www.iq.opengenus.org/'
        full_text = intro_text+'\n'+text+'\n'+outro_text
        with open(topic_name.get_text()+'.txt', 'a') as f:
            for word in full_text:
                try:
                    f.write(word)
                except:
                    f.write('error'+"\n")

        name=topic_name.get_text()+" raw.mp3"
        newpath2=output_file_location.split("//")
        newpath=output_file_location.split("//")
        newpath.append(name)
        output_file_location="\\".join(newpath)
        language = 'en'
        speech = gTTS(text=full_text, lang=language, slow=False)
        speech.save(output_file)
        os.system("mpg321 hello.mp3")
        output_file_location="//".join(newpath2)
        print(f"Converted URL {i} to raw audio")
        i+=1
    print("Converted all URLs to raw audio")
        
    


# In[49]:


input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
output_file_location="C:\\Users\\Ambarish Deb\\Desktop"
url_to_raw_audio(input_urls_file,output_file_location)


# In[74]:


def url_to_raw_text(input_urls_file, output_file_location):
    import requests
    from bs4 import BeautifulSoup
    with open(input_urls_file,'r') as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    i=1
    for url in urls:
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
            elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        #print(text)
        topic_name = soup.find('h1',class_='post-full-title')
        name=topic_name.get_text()+" raw.txt"
        newpath2=output_file_location.split("//")
        newpath=output_file_location.split("//")
        newpath.append(name)
        output_file_location="\\".join(newpath)
        with open(output_file_location, "w", encoding="utf-8") as text_file:
             text_file.write(text)
        output_file_location="//".join(newpath2)
        print(f"Converted URL {i} to raw text")
        i+=1
    print("successfully converted all URLs to raw text file!")


# In[75]:


input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
output_file_location="C:\\Users\\Ambarish Deb\\Desktop"
url_to_raw_text(input_urls_file, output_file_location)


# In[58]:


def url_to_text_summary(input_urls_file,output_file_location):
    import requests
    from bs4 import BeautifulSoup
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    with open(input_urls_file,'r') as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    i=1
    for url in urls:
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
             elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        topic_name = soup.find('h1',class_='post-full-title')
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, 10)
        text_summary = ""
        for sentence in summary:
            text_summary += str(sentence)
        intro_text = f'Today we will learn about {topic_name.text} '
        outro_text=f'\nThis was all about {topic_name.text} . For code files and additional information, please visit www.iq.opengenus.org/'
        text_summary = intro_text+'\n'+text_summary+'\n'+outro_text
        topic_name = soup.find('h1',class_='post-full-title')
        name=topic_name.get_text()+" summarised.txt"
        newpath2=output_file.split("//")
        newpath=output_file.split("//")
        newpath.append(name)
        output_file="\\".join(newpath)
        with open(output_file, "w", encoding="utf-8") as text_file:
             text_file.write(text)
        output_file="//".join(newpath2)
        print(f"Converted URL {i} to summarised text")
        i+=1
    print("successfully converted all URLs to summarised text!")


# In[59]:


input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
output_file_location="C:\\Users\\Ambarish Deb\\Desktop"
url_to_text_summary(input_urls_file,output_file)


# In[69]:


def text_to_summary(input_file,output_file_full_name):
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    with open(input_file, 'r', encoding="utf-8") as file:
        text = file.read()
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 10)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
    
    with open(output_file, "w", encoding="utf-8") as text_file:
        text_file.write(text_summary)


# In[70]:


input_file="C:\\Users\\Ambarish Deb\\Desktop\\POS Tagging in NLP using Python raw.txt"
output_file_full_name="C:\\Users\\Ambarish Deb\\Desktop\\sum.txt"
text_to_summary(input_file,output_file_full_name)


# In[94]:


get_ipython().system('pip install --upgrade pip')


# In[95]:


get_ipython().system('pip install speech_recognition')


# In[87]:


get_ipython().system('pip install opencv-python')


# In[88]:


get_ipython().system('pip install ffmpeg')


# In[96]:


import cv2
import numpy as np
import speech_recognition as sr

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    return r.recognize_google(audio)

def audio_to_video(input_file, output_file):
    # Transcribe the audio
    text = transcribe_audio(input_file)

    # Read the video file
    video = cv2.VideoCapture("video.mp4")

    # Get the video properties
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Create the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    # Iterate through each frame of the video
    while video.isOpened():
        ret, frame = video.read()

        if not ret:
            break

        # Add text to the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2
        text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        text_x = int((frame_width - text_size[0]) / 2)
        text_y = int((frame_height + text_size[1]) / 2)
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

        # Write the frame to the output video
        out.write(frame)

    # Release the resources
    video.release()
    out.release()
    cv2.destroyAllWindows()


# In[ ]:


def translate_text_file(input_file, output_file):
    from googletrans import Translator
    from googletrans import LANGUAGES
    if input("Show Supported Languages and their code? (yes/no): ").lower()=="yes":
        print("Supported Languages:")
        for code, language in LANGUAGES.items():
            print(f"{code}: {language}")
    src_lang=input("enter source language code: ")
    dest_lang=input("enter destination language code: ")
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    translator = Translator(service_urls=['translate.google.com'])

    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text.text)

# Example usage
translate_text_file('input.txt', 'output.txt')


# In[97]:


import argparse


parser = argparse.ArgumentParser(description='Data Conversion from command line')

parser.add_argument('-f')
parser.add_argument('--from', dest='input_type', required=True,
                    help='Specify the input type: "url","text" or "audio".  If converting from text or audio, ensure to write the full name of the output file. Else just mention the directory where the output should be located.')
parser.add_argument('--to', dest='output_type', required=True,
                    help='Specify the output type: "audio","summarised audio", "text","translated text", "summarised text", "video".')
parser.add_argument('--input', dest='input_file', required=True,
                    help='Specify the input data: URL file or text content')
parser.add_argument('--output', dest='output_file', required=True,
                    help='Specify the output file path for audio or summary')


args = parser.parse_args()


input_type = args.input_type.lower()
output_type = args.output_type.lower()
input_data = args.input_file
output_file = args.output_file


if input_type == 'url' and output_type == 'audio':
    url_to_raw_audio(input_file, output_file)
elif input_type == 'url' and output_type == 'summarised audio':
    url_to_summarised_audio(input_file, output_file)
elif input_type == 'url' and output_type == 'text':
    url_to_text(input_file,output_data)
elif input_type == 'url' and output_type == 'summarised text':
     url_to_text_summary(input_file,output_data)
elif input_type == 'text' and output_type == 'audio':
    text_to_audio(input_file,output_file)
elif input_type == 'text' and output_type == 'summary':
    text_to_summary(input_file,output_file)
elif input_type == 'text' and output_type == 'translated text':
    translate_text_file(input_file,output_file)
elif input_type == 'audio' and output_type == 'video':
    audio_to_video(input_data)
else:
    print('''please enter proper arguements. supported operations-\n1.url to raw_audio\n2.url to summarised_audio\n3.url to raw text\n4.url to summarised text\n5.text to audio\n6.text to summary\n7.audio to video\n8.Translate text''')


# In[ ]:


get_ipython().run_line_magic('tb', '')


# In[ ]:




