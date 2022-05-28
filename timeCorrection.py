import readTime
import cv2
import datetime


def datecorrection(path,x1,x2,y1,y2):
    video = cv2.VideoCapture(path)
    max_length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    seconds = int(max_length / fps)
    start,end= readTime.readTime(path,0,x1,y1,x2-x1,y2-y1),readTime.readTime(path,max_length-1,x1,y1,x2-x1,y2-y1)
    if start=='N/A' and end=='N/A':
        return 'N/A','N/A'
    elif start=='N/A':
        start=datetime.datetime.strptime(end,"%m/%d/%Y %H:%M:%S")-datetime.timedelta(seconds=seconds)
        start=start.strftime("%m/%d/%Y %H:%M:%S")
    elif end=='N/A':
        end=datetime.datetime.strptime(start,"%m/%d/%Y %H:%M:%S")+datetime.timedelta(seconds=seconds)
        end=end.strftime("%m/%d/%Y %H:%M:%S")
    return start,end



x1,x2,y1,y2=240,535,18,50
#print(readTime.readTime('5109.3.mp4',0,x1,y1,x2-x1,y2-y1))
print(datecorrection('5409.8.mp4',240,535,18,50))
#print(datecorrection('https://igct.s3.amazonaws.com/5fee675583dbb051a5aa4b16_1609762576.mp4',465, 488,0,703))
#with open('a.txt','r') as input_file:
#    lines=input_file.readlines()
#    i=0
#    for line in lines:
#        i+=1
#        line=line.strip()
#        print(i,datecorrection(line,465, 488,0,703))