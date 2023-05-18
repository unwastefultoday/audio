# audio

## steps to use (for jupyter notebooks)
1. Install jupyter notebooks
2. Download and run the .ipynb file
3. the output audio shall be saved at your working directory.

# the following content is for opengenus script.py

## dependencies
please ensure that these libraries are installed, updated and usable in your environment.
1. os
2. gTTS
3. requests
4. beautifulsoup
5. PlaintextParser from sumy.parsers.plaintext
6. Tokenizer from sumy.nlp.tokenizers
7. TextRankSummarizer from sumy.summarizers.text_rank
8. opencv
9. ffmpeg
10. numpy
11. speech-recognition
12. Translator and LANGUAGES from googletrans

## how to use 
opengenus script.py contains implementations of various functions to convert, summarise and translate data and to make these functions usable by command line.

once run successfully, you can use them from your local command line interface. 

 ### supported operations are- 
 1.url to raw_audio
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
