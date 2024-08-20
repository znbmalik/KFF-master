#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the necessary packages
import numpy as np
import cv2
import colorsys
def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
    # return the histogram
    return hist



def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    mylist=[]
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
    # loop over the percentage of each cluster and the color of
    # each cluster
    #for (percent, color) in sorted(zip(hist, centroids)):#, reverse=True
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX
        (h, s, v) = colorsys.rgb_to_hsv(color[0]/255, color[1]/255, color[2]/255)
        (h, s, v) = (int(h * 360), s, v)
        #print(percent, color)# return the bar chart
        mylist.append((percent,h, s, v))
    #return bar
    return mylist

# In[ ]:




