# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:42:17 2021

@author: JiHyeunKim
"""
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax

def get_data() :
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize = False, one_hot_label = False)
    return x_test, t_test

def init_network() :
    with open("sample_weight.pkl", 'rb') as f :
        network = pickle.load(f)
        
        return network
    
def predict(network, x) :
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y


x, t = get_data()
network = init_network()

#10000번 돈다.
accuracy_cnt = 0
for i in range(len(x)) :
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1
        
print("Accuracy : " + str(float(accuracy_cnt) / len(x)))
