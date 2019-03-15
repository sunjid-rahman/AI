# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:28:23 2019

@author: sunjid
"""
import numpy as np
import random
from collections import Counter
import math
def euclidean_distance(point1,point2):
    sum_squared_dist=0
    for i in range(len(point1)):
        sum_squared_dist+=math.pow(point1[i]-point2[i],2)
    return math.sqrt(sum_squared_dist)
    
def check_validation(valid,train):
    count=0
    for sample in valid:
        neigbr_dist_and_val=[]
        for example in train:
            dist=euclidean_distance(sample[:-1],example[:-1])
            neigbr_dist_and_val.append([dist,example[4]])
        sorted_neigbr_dist_and_val=sorted(neigbr_dist_and_val)
        k_nearest_dist_and_val=sorted_neigbr_dist_and_val[:20]
        print(sample)
        cls0=0
        cls1=0
        cls2=0
        for i in k_nearest_dist_and_val:
            if i[1]==0.0:
                cls0=cls0+1
            elif i[1]==1.0:
                cls1=cls1+1
            elif i[1]==2.0:
                cls2=cls2+1
                
        if cls0>=cls1 and cls0>=cls2:
            print(0)
            if sample[4] == 0.0:
                count=count+1
        elif cls1>=cls0 and cls1>=cls2:
            print(1)
            if sample[4] == 1.0:
                count=count+1
        else:
            print(2)
            if sample[4] == 2.0:
                count=count+1
    accuracy=(count/len(valid))*100
    print(len(valid))
    print(count)
    print("Accuracy of validity: "+str(accuracy))
def check_test(train,test):
    count=0
    for sample in test:
        neigbr_dist_and_val=[]
        for example in train:
            dist=euclidean_distance(sample[:-1],example[:-1])
            neigbr_dist_and_val.append([dist,example[4]])
        sorted_neigbr_dist_and_val=sorted(neigbr_dist_and_val)
        k_nearest_dist_and_val=sorted_neigbr_dist_and_val[:20]
        print(sample)
        cls0=0
        cls1=0
        cls2=0
        for i in k_nearest_dist_and_val:
            if i[1]==0.0:
                cls0=cls0+1
            elif i[1]==1.0:
                cls1=cls1+1
            elif i[1]==2.0:
                cls2=cls2+1
                
        if cls0>=cls1 and cls0>=cls2:
            print(0)
            if sample[4] == 0.0:
                count=count+1
        elif cls1>=cls0 and cls1>=cls2:
            print(1)
            if sample[4] == 1.0:
                count=count+1
        else:
            print(2)
            if sample[4] == 2.0:
                count=count+1
    accuracy=(count/len(test))*100
    print(len(test))
    print(count)
    print("Accuracy of Test: "+str(accuracy))    
def main():
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
            
    #print(len(Test))
    train=np.array(Train)
    test=np.array(Test)
    valid=np.array(Valid)
    check_validation(valid,train)
    check_test(train,test)
    

        
        
        
main()
