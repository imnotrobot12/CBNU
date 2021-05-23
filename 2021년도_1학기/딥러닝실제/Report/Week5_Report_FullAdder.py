# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:23:26 2021

@author: JiHyeunKim
"""
import numpy as np

def AND(x1, y1) :
    x = np. array([x1, y1])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
    

def NAND(x1, y1) :
    x = np.array([x1, y1])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    

def OR(x1, y1) :
    x = np.array([x1, y1])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, y1) :
    s1 = NAND(x1, y1)
    s2 = OR(x1, y1)
    out = AND(s1, s2)
    return out

def Full_Adder(x, y, z) :
    First_Layer_XOR = XOR(x, y)
    First_Layer_AND = AND(x, y)
    
    Second_Layer_AND = AND(First_Layer_XOR, z)
    
    Sum = XOR(First_Layer_XOR, z)
    Carry = OR(Second_Layer_AND, First_Layer_AND)
    
    return Sum ,Carry

def Check_Input_Value(value):
    if value > 1 or value < 0 :
        print('0과 1만 입력해주세요. 강제로 0을 입력합니다.')
        return True

x = int(input('x = '))
Check = Check_Input_Value(x)
if Check == True:
    x = 0
    print('x = 0')


y = int(input('y = '))
Check = Check_Input_Value(y)
if Check == True:
    y = 0
    print('y = 0')

z = int(input('z = '))
Check = Check_Input_Value(z)
if Check == True:
    z = 0
    print('z = 0')

Full_Adder(x, y, z)

OutSum, OutCarry = Full_Adder(x, y, z)

print(' SUM = ', OutSum, ' CARRY = ', OutCarry)


    
    