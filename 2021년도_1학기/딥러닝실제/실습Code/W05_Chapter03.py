# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:51:33 2021

@author: JiHyeunKim
"""
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x) :
    return 1/(1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


