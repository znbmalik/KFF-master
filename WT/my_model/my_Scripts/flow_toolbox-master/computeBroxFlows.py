#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2

baseDir = '../../my_data/UCF50'
outputDir = '../../my_data/UCF50-OP/flows/jpg/'


def createDirectories(processed_vid):           
    if not os.path.exists(processed_vid):
        os.makedirs(processed_vid)
    else:
        files = os.listdir(processed_vid)
        for f in files:
            if os.path.isfile(os.path.join(processed_vid,f)):
                os.remove(os.path.join(processed_vid,f))
                
for cls in os.listdir(baseDir):
    
    print("cls",cls)
    current_path = os.path.join(baseDir, cls)

    # Check if it's a file and has the name ".DS_Store"
    if os.path.isfile(current_path) and cls == ".DS_Store":
        continue;
        print("file :", cls)
        
    classPath=os.path.join(baseDir,cls)
    
    for videoName in os.listdir(classPath):
        
        videoPath=os.path.join(classPath,videoName)
        print(videoName)

        
        flowPath=os.path.join(outputDir,cls,videoName.split('.')[0]+".avi")
        vidcap = cv2.VideoCapture(videoPath)
        property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
        length = int(cv2.VideoCapture.get(vidcap, property_id))
        #print( length )
        #print(videoPath)
        #print(flowPath)
        
        createDirectories(flowPath)
        
       
        os.system('./flow_video -v 1 -b 1 -e '+str(length-1)+' -o '+flowPath+' '+videoPath)
        #os.system('./flow_video -v 1 -b 3 -e 63 -o '+flowPath+' '+videoPath)
        
        
    


# In[ ]:




