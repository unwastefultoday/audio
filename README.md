# audio

## dependencies
please ensure that these libraries mentioed at requirements.text are installed and usable.
## how to use 
opengenus_convertor.py.py contains implementations of various functions to convert, summarise and translate data and to make these functions usable by command line.

once run successfully, you can use them from your local command line interface. 

 ### supported operations are- 
 **1.url to raw_audio-**<br>
 for availing this use case, run the function url_to_raw_audio. <br>
Command Line Statement:  **python opengenus_convertor.py --from=URL --to=audio**<br>
 Sample Input - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">a file containing a list of URLs</a><br>
 Sample Output - <a href ="https://drive.google.com/drive/folders/1HjFOxJ09OoHHtX5823pdThG16tZvytSz">converted audio files at the working directory</a><br><br>
 
 **2.url to summarised_audio**<br>
 for availing this use case, run the function url_to_summarised_audio. <br>
Command Line Statement:  **python opengenus_convertor.py --from=URL --to=summarised audio**<br>
 Sample Input - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">a file containing a list of URLs</a><br>
 Sample Output - <a href ="https://drive.google.com/drive/folders/1HFpqzDkw6fIHtBRp-4anwmO4qyzjXg0q?usp=sharing">converted and summarised audio files at the working directory</a><br><br>
 
 **3.url to raw text**<br>
  for availing this use case, run the function url_to_raw_text. <br>
  Command Line Statement:  **python opengenus_convertor.py --from=URL --to=text**<br>
  Sample Input - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">a file containing a list of URLs</a><br>
  Sample Output - <a href ="https://drive.google.com/drive/folders/18E11QnYvJWz_FTQmBesEbeA6dUH7HlBF?usp=sharing">converted text files at the  working directory</a><br><br>
  
 **4.url to summarised text**<br>
 for availing this use case, run the function url_to_text_summary. <br>
  Command Line Statement:  **python opengenus_convertor.py --from=URL --to=summarised text**<br>
  Sample Input - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">a file containing a list of URLs</a><br>
  Sample Output - <a href ="https://drive.google.com/drive/folders/1zZprOJk2HTWMW6gIYY-ftuhP51MQpFSO?usp=sharing">converted and summarized text files at the  working directory</a><br><br>
 **5.text to summary**<br>
  for availing this use case, run the function text_to_summary. <br>
  Command Line Statement:  **python opengenus_convertor.py --from=text --to=summarised text**<br>
  Sample Input - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">a text file</a><br>
  Sample Output - <a href ="https://drive.google.com/drive/folders/1zZprOJk2HTWMW6gIYY-ftuhP51MQpFSO?usp=sharing">summarised content at the  working directory</a><br><br>
 **6.audio to video**<br>
 **7.Translate text**<br>
 
 ### keywords -
"URL","text","audio","summarised audio", "text","translated text", "summarised text", "video"
 
 A sample command is - 

#### python filename.py --from=URL --to=audio"

it takes a file of URLs as input and converts them to audio at a specified location. 

If converting from text or audio, ensure to write the full name of the output file. Else just mention the directory where the output should be located.
