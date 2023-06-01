# audio

## dependencies
please ensure that these libraries mentioed at requirements.text are installed and usable.
## how to use 
opengenus_convertor.py.py contains implementations of various functions to convert, summarise and translate data and to make these functions usable by command line.

once run successfully, you can use them from your local command line interface. 

 ### supported operations are- 
 **1.url to raw_audio-**
 for availing this use case, run the function url_to_raw_audio through the command line statement - 
 **python opengenus_convertor..py --from=URL --to=audio**
 Sample Input - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">a file containing a list of URLs</a>
 Sample Output - <a href ="https://drive.google.com/file/d/1jv2acLzs_1Ykm1wwZV-JfhxMzEGGukZr/view?usp=sharing">converted audio files at the working directory</a>
 
 <br>
 2.url to summarised_audio
 3.url to raw text
 4.url to summarised text
 5.text to audio
 6.text to summary
 7.audio to video
 8.Translate text.
 
 ### keywords -
"URL","text","audio","summarised audio", "text","translated text", "summarised text", "video"
 
 A sample command is - 

#### python filename.py --from=URL --to=audio"

it takes a file of URLs as input and converts them to audio at a specified location. 

If converting from text or audio, ensure to write the full name of the output file. Else just mention the directory where the output should be located.
