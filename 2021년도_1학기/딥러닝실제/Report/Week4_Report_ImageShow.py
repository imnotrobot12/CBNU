# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:58:47 2021

@author: JiHyeunKim
"""
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('..\Report\증명사진.jpg')

plt.imshow(img)
plt.show()
