#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the necessary packages
from sklearn.cluster import KMeans
import tensorflow as tf
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import os
import shutil
from PIL import Image

folder='../../my_data/UCF-Brox/Full-Flow-All-UCF101/rgb/jpg/'
outputfolder='../../my_data/UCF-Brox/Full-KeyFlow-All-UCF101/rgb/jpg/'


# In[2]:


def histImage(image):
    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster the pixel intensities
    clt = KMeans(n_clusters = 7, max_iter=10)
    clt.fit(image)
    
    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    #print("hist", hist)
    #print("clt.cluster_centers_",clt.cluster_centers_)
    bar = utils.plot_colors(hist, clt.cluster_centers_)
    
    return bar 
    


# In[3]:


def compareHSV(bar0, bar1, a_margin=0, nc_margin=0, m_margin=0):
    newColor=[]
    for b in bar1:
        
        flag=False
        for bb in bar0:
            if (abs(b[1]-bb[1])<=a_margin) and (abs(b[2]-bb[2])<=m_margin):
                flag=True       
                
        if flag==False:#new color not in range of any exiting color
            if b[0] > nc_margin  or b[2] > m_margin:
                newColor.append(b)
            
    
    for b in bar0:
        flag1=False
        for bb in bar1:
            if (abs(b[1]-bb[1])<=a_margin) and (abs(b[2]-bb[2])<=m_margin):
                flag1=True       
                
        if flag1==False:#new color not in range of any exiting color
            if b[0] > nc_margin or b[2] > m_margin:
                newColor.append(b)
    return newColor
            
                


# In[4]:


def excludeBK(bar):
    foregroundBar=[]
    
    for b in bar:
        foregroundBar.append((b[0],b[1],b[2]*b[3]))
    #return foregroundBar
    sorted_list = sorted(foregroundBar,key=lambda t: t[2])
    
    if sorted_list[0][0]>0.5:
        sorted_list.pop(0)
    #print(sorted_list)
    return sorted_list


# In[5]:


def createDirectories(processed_vid):           
    if not os.path.exists(processed_vid):
        os.makedirs(processed_vid)
    else:
        files = os.listdir(processed_vid)
        for f in files:
            if os.path.isfile(os.path.join(processed_vid,f)):
                os.remove(os.path.join(processed_vid,f))





for action in os.listdir(folder):
    
    actiobclass=os.path.join(folder,action)
    print(actiobclass)
    for vid in os.listdir(actiobclass):
        if vid.endswith('.avi'):
            vidName=os.path.join(actiobclass,vid)
            print(vidName)
            outputPath=os.path.join(outputfolder,action, vid)
            createDirectories(outputPath)
            flows_path=[]
            keyframes=[]
            for opticalFow in os.listdir(vidName):
                if opticalFow.endswith(".jpg"):
                    opticalFlow=os.path.join(vidName,opticalFow)
                    flows_path.append(opticalFlow)

            flows_path.sort(key = lambda x: int(x.split('.')[-2].split('_')[-1]))
            #for x in flows_path:
            #    print(x)
            image1=cv2.imread(flows_path[0])
            image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            #down Sample
           
            image1 = cv2.pyrDown(image1)
            
            keyframes.append(flows_path[0])
            for image in range(1, len(flows_path)):
                print(flows_path[image])
                image=flows_path[image]
                
                
                bar0=histImage(image1)

                image2 = cv2.imread(image) 
                image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB) 
                #down Sample
                image2= cv2.pyrDown(image2)
                
                bar1=histImage(image2)

                bar0=excludeBK(bar0) 
                bar1=excludeBK(bar1)

                if len(compareHSV(bar0, bar1,15,0.2,0.2)) > 1:
                    keyframes.append(image)
                    image1=image2
                 
            print(len(keyframes))
            for i in keyframes:
                #print(i)
                shutil.copy(i, os.path.join(outputPath,i.split(os.path.sep)[-1]))
                #print(os.path.join(outputPath,i.split(os.path.sep)[-1]))
            


# In[ ]:




