# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 18:02:01 2015

@author: lenovo
"""
import numpy as np
import cv2
img = cv2.imread('Capture.PNG',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()