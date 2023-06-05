def process_file_path(file_path):
    import os
    # Convert the file path to an absolute path if it is relative
    if not os.path.isabs(file_path):
        linkingpath = input("Enter full path till BEFORE required location/file separated by double forward slashes: ")
        os.chdir(linkingpath)
        current_dir = os.getcwd()  # Get the current working directory
        full_file_path = os.path.join(current_dir, file_path)  # Create the absolute path
    else:
        full_file_path=file_path
    return full_file_path




def url_to_summarised_audio(input_urls_file,output_file_location):
    from gtts import gTTS
    import requests
    from bs4 import BeautifulSoup
    import re
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    import os
    input_urls_file=process_file_path(input_urls_file)
    output_file_location=process_file_path(output_file_location)
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
        
    


# In[5]:


#input_urls_file="Desktop\\project\\input.txt"
#output_file_location="Desktop"
#url_to_summarised_audio(input_urls_file,output_file_location)


# In[ ]:


def url_to_raw_audio(input_urls_file,output_file_location):
    from gtts import gTTS
    import requests
    from bs4 import BeautifulSoup
    import re
    import os
    input_urls_file=process_file_path(input_urls_file)
    output_file_location=process_file_path(output_file_location)
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
        speech.save(output_file_location)
        os.system("mpg321 hello.mp3")
        output_file_location="//".join(newpath2)
        print(f"Converted URL {i} to raw audio")
        i+=1
    print("Converted all URLs to raw audio")
        
    


# In[ ]:


#input_urls_file="Desktop\\project\\input.txt"
#output_file_location="Desktop"
#url_to_raw_audio(input_urls_file,output_file_location)


# In[ ]:


def url_to_raw_text(input_urls_file, output_file_location):
    import requests
    from bs4 import BeautifulSoup
    input_urls_file=process_file_path(input_urls_file)
    output_file_location=process_file_path(output_file_location)
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


# In[ ]:


#input_urls_file="Desktop\\project\\input.txt"
#output_file_location="Desktop"
#url_to_raw_text(input_urls_file, output_file_location)


# In[ ]:


def url_to_text_summary(input_urls_file,output_file_location):
    import requests
    from bs4 import BeautifulSoup
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    input_urls_file=process_file_path(input_urls_file)
    output_file_location=process_file_path(output_file_location)
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
        newpath2=output_file_location.split("//")
        newpath=output_file_location.split("//")
        newpath.append(name)
        output_file="\\".join(newpath)
        with open(output_file, "w", encoding="utf-8") as text_file:
             text_file.write(text)
        output_file="//".join(newpath2)
        print(f"Converted URL {i} to summarised text")
        i+=1
    print("successfully converted all URLs to summarised text!")


# In[ ]:


#input_urls_file="Desktop\\project\\input.txt"
#output_file_location="Desktop"
#url_to_text_summary(input_urls_file,output_file_location)





def text_to_summary(input_file,output_file_full_name):
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    input_file=process_file_path(input_file)
    output_file_full_name=process_file_path(output_file_full_name)
    with open(input_file, 'r', encoding="utf-8") as file:
        text = file.read()
    output_file = output_file_full_name.split("//")[-1]
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 10)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
    
    with open(output_file_full_name, "w", encoding="utf-8") as text_file:
        text_file.write(text_summary)





#input_file="Desktop\\POS Tagging in NLP using Python raw.txt"
#output_file_full_name="Desktop\\sum.txt"
#text_to_summary(input_file,output_file_full_name)




get_ipython().system('pip install --upgrade pip')


# In[ ]:


get_ipython().system('pip install opencv-python')


# In[ ]:


get_ipython().system('pip install ffmpeg')


# In[ ]:


get_ipython().system('pip install SpeechRecognition')


# In[ ]:


get_ipython().system('pip install moviepy')





from moviepy.editor import AudioFileClip, VideoClip,TextClip,CompositeVideoClip
import numpy as np
def convert_audio_to_video(input_file, output_file):
    input_file=process_file_path(input_file)
    output_file=process_file_path(output_file)
    audio = AudioFileClip(input_file)
    name = input_file.split("\\")[-1][:-4]

    # Create a blank video clip with the same duration as the audio
    video = VideoClip(lambda t: np.zeros((640, 480, 3), dtype=np.uint8), duration=audio.duration)

    # Set the audio of the video clip to the provided audio file
    video = video.set_audio(audio)

    # Set the video duration to match the audio duration
    video = video.set_duration(audio.duration)
    
    text_clip = TextClip(name, fontsize=30, color='white', size=(640,480))
    text_clip = text_clip.set_duration(audio.duration)
    text_clip = text_clip.set_position(('center', 'center'))

    # Composite the video clip and text together
    final_video = video.set_duration(audio.duration).set_position(('center', 'center'))
    
    final_video = CompositeVideoClip([final_video, text_clip])

    # Set the video filename and write it to the output file location
    final_video.write_videofile(output_file, codec='libx264',fps=24)





# Example usage
#convert_audio_to_video('Desktop\\Paraphrasing in NLP Summarised.mp3', 'Desktop\\output.mp4')





get_ipython().system('pip install googletrans')





def translate_text_file(input_file, output_file):
    from googletrans import Translator
    from googletrans import LANGUAGES
    if input("Show Supported Languages and their code? (yes/no): ").lower()=="yes":
        print("Supported Languages:")
        for code, language in LANGUAGES.items():
            print(f"{code}: {language}")
    src_lang=input("enter source language code: ")
    dest_lang=input("enter destination language code: ")
    input_file=process_file_path(input_file)
    output_file=process_file_path(output_file)
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    translator = Translator(service_urls=['translate.google.com'])

    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text.text)

# Example usage
#translate_text_file('input.txt', 'output.txt')





import cv2
import numpy as np
from moviepy.editor import AudioFileClip

def convert_audio_to_video(input_file, output_file):
    input_file=process_file_path(input_file)
    output_file=process_file_path(output_file)
    audio = AudioFileClip(input_file)
    name = input_file.split("//")[-1][:-4]

    # Get the duration and frame rate of the audio
    duration = audio.duration
    fps = audio.fps

    # Create a blank video with the same duration as the audio
    width, height = 640, 480
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Add text to each frame of the video
    for t in np.arange(0, duration, 1/fps):
        # Create a blank frame
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Add the text to the frame using OpenCV
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_position = (int(width / 2 - len(name) * 5), int(height / 2))
        cv2.putText(frame, name, text_position, font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Write the frame to the video
        writer.write(frame)

    # Release the video writer
    writer.release()

# Example usage
#convert_audio_to_video('Desktop\\POS Tagging in NLP using Python summarised.mp3', '\Desktop\\output+text.mp4')


# In[ ]:


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
elif input_type == 'url' and output_type == 'summary':
     url_to_text_summary(input_file,output_data)
elif input_type == 'text' and output_type == 'summary':
    text_to_summary(input_file,output_file)
elif input_type == 'text' and output_type == 'summaryised text
    text_to_summary(input_file,output_file)
elif input_type == 'text' and output_type == 'translated text':
    translate_text_file(input_file,output_file)
elif input_type == 'audio' and output_type == 'video':
    convert_audio_to_video(input_data)
else:
    print('''please enter proper arguements.''')







