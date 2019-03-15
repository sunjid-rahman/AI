# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:55:02 2019

@author: Sunjid Rahman
"""
import numpy as np
import matplotlib.pyplot as plt
def logistic_regression_training(train):
    for iteration in range(0,30000):
        total_loss=0,total_dj_by_dt=0
        for sample in train:
            j=(-y*np.log(h)-(1-y)*np.log(1-h))
            dj_by_dt=x(h-y)
            total_loss=total_loss+j
            total_dj_by_dt=total_dj_by_dt+dj_by_dt
        avg_loss=1/m*total_loss
        avg_total_dj_by_dt=1/m*total_dj_by_dt
        dt=dt-lr*dj_by_dt
        print(avg_loss)
            

def main():
    #iris = datasets.load_iris()
    #X = iris.data[:, :2]
    #y = (iris.target != 0) * 1
   # plt.figure(figsize=(10, 6))
    #plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
    #plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
    #plt.legend();
    lines=[]
    with open('C:/Users/Sunjid Rahman/Desktop/iris_dataset.txt') as f:
        lines=f.read().splitlines()
    #print(lines[0:4])
    
    wanted_lines=[]
    for i in range(0,len(lines)):
        line=lines[i].split(",")
        wanted_lines.append(line)
   # print(wanted_lines[0:4])
    
    outputs=[]
    for i in range(0,len(wanted_lines)):
        outputs.append(wanted_lines[i][-1])
    output_set=set(outputs)
    #print(output_set)
    
    output_dict={}
    i=0
    for element in output_set:
        #print(element)
        output_dict[element]=i
        i=i+1
    #print(output_dict)
    
    for i in range(0,len(wanted_lines)):
        wanted_lines[i][-1]=output_dict[wanted_lines[i][-1]]
    #print(wanted_lines[0:4])
        
    for i in range(0,len(wanted_lines)):
        for j in range(0,len(wanted_lines[0])):
            wanted_lines[i][j]=float(wanted_lines[i][j])
    #print(np.array(wanted_lines))
    Train=[]
    Test=[]
    Valid=[]
    for i in range(0,len(wanted_lines)):
        num=random.uniform(0,1)
        if(num>0.7 and num<=0.85):
            Valid.append(wanted_lines[i])
        elif(num>0.85 and num <=1.0):
            Test.append(wanted_lines[i])
        else:
            Train.append(wanted_lines[i])
            
    train=np.array(Train)
    test=np.array(Test)
    valid=np.array(Valid)
    logistic_regression_training(train)
main()
    