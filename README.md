# datecorrection

# Introduction to algorithm
 This algorithm is used to correct start & end time for events(trespassing,train,signal). Before running the code, please download both readTime.py and timeCorrection.py. In addition, you need to download PyTesseract library on you local machine. See https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac for downloading the library. 
 
 After download all necessary packages, please change line 7 of readTime.py to the directory where your PyTesseract is installed.
 
 To get start and end time, you need to import timeCorrection.py and call the function datecorrection(path,x1,x2,y1,y2). Input parameters are as follow:
path: video link or the directory of the video.
x1: x coordinate of the upper left point of the bounding box for the timestamp.
x2: x coordinate of the lower right point of the bounding box for the timestamp.
y1: y coordinate of the upper left point of the bounding box for the timestamp.
y2: y coordinate of the lower right point of the bounding box for the timestamp.


### For Thomasville North/South, Ramsey, and Ashland, the coordinates are:

Thomasville North/South & Ashland: x1=0, x2=43, y1=0, y2=1300

Ramsey: x1=465, x2=488, y1=0, y2=703

### Return value
The function will return two strings. The first one is start time, and the second one is end time.All strings aare in the correct time format: Month/Day/Year Hour:Minute:Second. If both string are incorrect, the function would change the string to "N/A". If only one of the string is invalid, then the program would replace the incorrect value with a calculated the time using video time and the correct timestamp.
For example, the possible format for return value: ('06/04/2021 11:27:17', '06/04/2021 11:27:24'), or ('N/A', 'N/A').
