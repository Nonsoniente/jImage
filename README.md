# jImage
 Python script to hide any kind of file in an image (and extract it)

This is for educational purposes only, I am not responsible for anything that you do with this script

# Requirements

Note: to hide a file in an image the image file should be at least 8 times the file's one (in future there will be the option to split the file in pieces)

# How to use

The usage is simple:

To hide a simple string of text, use:

<code> EncodeText(imagePath,text) </code> 

To hide a file, use:

<code> EncodeFile(imagePath,filePath) </code>



Those lines will both generate a modified version of the image, called "Encoded.png", which contains the text/file.



Then, to extract a text use:

<code> DecodeText(imagePath,textLenght) </code>  

where "textLenght" is the lenght of the string that we want to extract. 

(if you don't know, try to guess, then adjust by seeing the result. 

For example, if after extracting you got a string like this: "hello world%%niovdacmkxld" probably the hidden text was just "hello world"

Or, if after extracting you got a string like this: "Hello wo", probably the hidden text was longer)



To extract a file, use:

<code> DecodeFile(imagePath,fileSize,extension) </code>

where "extension" is the extension of the file that we are extracting and "fileSize" is the size of the file that we are extracting (if you don't know, try to guess. 

If it gives you an error, probably the file was bigger, else, it should work)



