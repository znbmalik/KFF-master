#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import cv2
baseDir = '../../my_data/Penn_Action/flow/jpg/'


# In[12]:


for cls in os.listdir(baseDir):
    print(cls)
    classPath=os.path.join(baseDir,cls)
    for videoName in os.listdir(classPath):

        videoPath=os.path.join(classPath,videoName)
        print(videoPath)
        for flowName in os.listdir(videoPath):
            print(flowName)
            flowCount=int((flowName.split('_')[-1]).split('.')[0])
            print(flowCount)
            flowCount-=3
            flowPath=os.path.join(videoPath,flowName)
            flowNewName=videoName+'_{0:05d}.jpg'.format(int(flowCount))
            print(flowNewName)
            print(os.path.join(videoPath,flowNewName))
            print(os.path.join(videoPath,flowName))
            print(flowCount)
            os.rename(os.path.join(videoPath,flowName),os.path.join(videoPath,flowNewName))
        
        


# In[ ]:




