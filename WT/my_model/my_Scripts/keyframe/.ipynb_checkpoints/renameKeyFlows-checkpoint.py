#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os
folder='../../my_data/UCF50_flowNet/UCF50-KeyFlow_15/flow/jpg/'


for action in os.listdir(folder):
    
    actiobclass=os.path.join(folder,action)
    print(actiobclass)
    for vid in os.listdir(actiobclass):
        # get the start time
        #print(vid)
        if vid.endswith('.avi'):
            vidName=os.path.join(actiobclass,vid)
            print(vidName)
            outputPath=os.path.join(folder,action, vid)
            print(outputPath)
            #createDirectories(outputPath)
            flows_path=[]
            keyframes=[]
            for opticalFow in os.listdir(vidName):
                if opticalFow.endswith(".jpg"):
                    opticalFlow=os.path.join(vidName,opticalFow)
                    flows_path.append(opticalFlow)
            if len(flows_path) > 0:
                flows_path.sort(key = lambda x: int(x.split('.')[-2].split('_')[-1]))
                #for x in flows_path:
                print(len(flows_path))
                #print(flows_path)
            
            counter=0
            for op in flows_path:
                print(op)
                flowName="/".join(op.split('/')[0:9])
                #print(flowName)
                flowName=flowName+"/"+(op.split('.')[-3]).split('/')[-1]+".avi_{0:0=5d}.jpg".format(counter)
                print(flowName)
                os.rename(op, flowName)
                counter+=1
                
            


# In[ ]:




