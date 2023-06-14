# audio

## dependencies
please ensure that these libraries mentioned at requirements.txt are installed and usable.

## addressing mode
Both relative and absolute addresses are supported, due to the use of the process_address function. However, the route from the root directory to the working folder will need to be established if relative addressing is used. 
## how to use 
opengenus_convertor.py contains implementations of various functions to convert, summarise and translate data and to make these functions usable by command line.

once run successfully, you can use them from your local command line interface. 

 ### supported operations are- 
 **1.url to raw_audio-**<br>
 for availing this use case, run the function url_to_raw_audio. <br>
Command Line Statement:  **python opengenus_convertor.py --from=URL --to=audio**<br>
Parameters: 2- input_urls_file and output_file_location, both address parameters. Output file is created from scratch, any existing file with same name is overwritten.
 Sample Input - <a href ="https://github.com/unwastefultoday/audio/blob/main/input/input.txt">a file containing a list of URLs</a><br>
 Sample Output - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/audio/raw%20audio">converted audio files at the working directory</a><br><br>
 
 **2.url to summarised_audio**<br>
 for availing this use case, run the function url_to_summarised_audio. <br>
Command Line Statement:  **python opengenus_convertor.py --from=URL --to=summarised audio**<br>
Parameters: 2- input_urls_file and output_file_location, both address parameters. Output file is created from scratch, any existing file with same name is overwritten.
 Sample Input - <a href ="https://github.com/unwastefultoday/audio/blob/main/input/input.txt">a file containing a list of URLs</a><br>
 Sample Output - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/audio/summarised%20audio">converted and summarised audio files at the working directory</a><br><br>
 
 **3.url to raw text**<br>
  for availing this use case, run the function url_to_raw_text. <br>
  Command Line Statement:  **python opengenus_convertor.py --from=URL --to=text**<br>
  Parameters: 2- input_urls_file and output_file_location, both address parameters. Output file is created from scratch, any existing file with same name is overwritten.
  Sample Input - <a href ="https://github.com/unwastefultoday/audio/blob/main/input/input.txt">a file containing a list of URLs</a><br>
  Sample Output - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/text/raw%20text">converted text files at the  working directory</a><br><br>
  
 **4.url to summarised text**<br>
 for availing this use case, run the function url_to_text_summary. <br>
  Command Line Statement:  **python opengenus_convertor.py --from=URL --to=summarised text**<br>
  Parameters: 2- input_urls_file and output_file_location, both address parameters. Output file is created from scratch, any existing file with same name is overwritten.
  Sample Input - <a href ="https://github.com/unwastefultoday/audio/blob/main/input/input.txt">a file containing a list of URLs</a><br>
  Sample Output - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/text/summarised%20text">converted and summarized text files at the  working directory</a><br><br>
 **5.text to summary**<br>
  for availing this use case, run the function text_to_summary. <br>
  Parameters: 2-Input_file,output_file_full_name. Here we need to specify name of the output file as well.
  Command Line Statement:  **python opengenus_convertor.py --from=text --to=summarised text**<br>
  Sample Input - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/text/raw%20text">a text file</a><br>
  Sample Output - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/audio/summarised%20audio">summarised content at the  working directory</a><br>
 **6.audio to video**<br>
   for availing this use case, run the function audio_to_video. <br>
   Parameters: 2- input_file, output_file, both address parameters of the input mp3 and output mp4 files, respectively. Output file is created from scratch, any existing file with same name is overwritten.
  Command Line Statement:  **python opengenus_convertor.py --from=audio --to=video**<br>
  Sample Input - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/audio/raw%20audio">an audio file</a><br>
  Sample Output - <a href ="https://github.com/unwastefultoday/audio/blob/main/input/video/video%20output.mp4">video file at the  working directory</a><br>                
 **7.Translate text**<br>
  for availing this use case, run the function translate_text_file. <br>
   Parameters: 2- input_file, output_file, both address parameters of the input and translated files, respectively. Output file is created from scratch, any existing file with same name is overwritten.
  Command Line Statement:  **python opengenus_convertor.py --from=text --to=translated text**<br>
  Sample Input - <a href =" for availing this use case, run the function translate_text_file. <br>
  Sample Input - <a href ="https://github.com/unwastefultoday/audio/blob/main/input/translation%20input.txt">an input file in english</a><br>
  Expected Output - <a href ="https://github.com/unwastefultoday/audio/tree/main/output/translation">translated in french </a><br>   

If converting from text or audio, ensure to write the full name of the output file. Else just mention the directory where the output should be located.

