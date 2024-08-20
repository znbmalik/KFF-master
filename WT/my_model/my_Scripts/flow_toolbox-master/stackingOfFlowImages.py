#!/usr/bin/env python
# coding: utf-8

# In[60]:


import os
import numpy as np
from PIL import Image




# In[61]:


def stackflows(input_path,input_path_flow,processed_vid,depth,interval):
    
    for file in os.listdir(input_path):
        print(file)
        flowList=[]
        flows=[]
        for f in os.listdir(os.path.join(input_path_flow)):

            if f.startswith(file):
                if f.endswith(".jpg"):
                    #print(f)
                    flowList.append(f)
        #print(len(flowList))
        flowList.sort(key = lambda x: x.split('.')[-2])
        #print(flowList)

        flows=[]
        count=0
        while count<32:

            a = Image.open(os.path.join(input_path_flow,flowList[count]))
            b = Image.open(os.path.join(input_path_flow,flowList[count+1]))
            #print(a.shape)
            a=np.array(a).astype('float64')
            
            min_val=np.min(a)#added
            max_val=np.max(a)#added
            a=255*(a-min_val)/(max_val-min_val)
            #a-=np.mean(a).astype('float64')
            
            b=np.array(b).astype('float64')
            min_val=np.min(b)#added
            max_val=np.max(b)#added
            b=255*(b-min_val)/(max_val-min_val)
            #b-=np.mean(b).astype('float64')
            
            #255*(inputChannel-min)/(max-min)
            m_flow=np.dstack((a,b))
            
            flows.append(m_flow)
            

            count+=2
            
        stacked=np.concatenate(flows, axis=2)
        stacked= np.transpose(stacked, (2, 0, 1))
        print(stacked.shape)
        min_val=np.min(stacked)#added
        max_val=np.max(stacked)#added

        if min_val!=max_val:
            vid_name=file.split('.')[0]
            np.save(processed_vid+vid_name+".npy", stacked)
            #np.save(vid_name+".npy", stacked)
        
        


# In[62]:


#******************************************folders for OF***********************************
def createDirectories(processed_vid):           
    if not os.path.exists(processed_vid):
        os.makedirs(processed_vid)
    else:
        files = os.listdir(processed_vid)
        for f in files:
            os.remove(os.path.join(processed_vid,f))
                   
    #******************************************folders for OF***********************************


# In[63]:


interval=1#1, 4 or 8
depth=2 #5,3,2,'RGB'
processed_vid='/home/my_model/my_data/Brox_Flow_StackedFrames/depth_'+str(depth)+'/'+str(interval)+'/'
input_path = '/home/my_model/my_data/depth_'+str(depth)+'/'+str(interval)
input_path_flow ='/home/my_model/my_data/FlowImages'
createDirectories(processed_vid)
stackflows(input_path,input_path_flow,processed_vid,depth,interval)


# In[ ]:




