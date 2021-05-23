# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:40:56 2021

@author: JiHyeunKim
"""
import numpy as np
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img) :
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
    
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize = False)

img = x_train[10]
label = t_train[10]
print(label)

print(img.shape)
img = img.reshape(28,28)
print(img.shape)

img_show(img)