#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
import cv2



import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os, cv2,sys



action='All'


# In[2]:


def createDirectories(processed_vid):           
    if not os.path.exists(processed_vid):
        os.makedirs(processed_vid)
    else:
        files = os.listdir(processed_vid)
        for f in files:
            os.remove(os.path.join(processed_vid,f))


# In[3]:


input_path="../../my_data/key_video"
for file in os.listdir(input_path):
    for vid in os.listdir(os.path.join(input_path,file)):
        folder_path="/home/my_model/my_data/Key-"+action+"-UCF101/flow/jpg/"+str(file)+"/"+str(vid.split('.')[0])
        createDirectories(folder_path)


# In[4]:


input_path="../../my_data/FlowImages"
for file in os.listdir(input_path):
    #print(file)
    #vid=file.split('.')[0]
    vid='_'.join((file.split('.')[0]).split('_')[0:4])
    output_path="../../my_data/Key-"+action+"-UCF101/flow/jpg/"+str(file.split('_')[1])+"/"+vid
    
    if file.endswith('jpg'):
        print(os.path.join(input_path, file))
        img = cv2.imread(os.path.join(input_path, file), cv2.IMREAD_UNCHANGED)
        print(output_path+'/'+file)
        cv2.imwrite(output_path+'/'+file, img)
        #shutil.copy(os.path.join(input_path, file), os.path.join(output_path, file))

    else: 
        shutil.copy(os.path.join(input_path, file), os.path.join(output_path, file))


# In[ ]:





# In[ ]:




