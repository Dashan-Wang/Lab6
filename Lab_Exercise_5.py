#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:41:40 2017

@author: wang
"""

#Lab Exercise 1
'''
import time
import random
import pylab as py

def timing(func,*args):
    a = time.time()
    func(*args)
    b = time.time()
    return b - a

def maximum(l):
    maximum = l[0]
    for i in range(len(l)):
        if l[i] > maximum:
            maximum = l[i]
    return maximum

def maximum_recursion(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], maximum_recursion(l[1:len(l)]))

limit = 100
time_ord = []
time_rec = []

for i in range(1,limit):
    input_l = [random.random() for x in range(i)]
    time_ord.append(timing(maximum,input_l))
    time_rec.append(timing(maximum_recursion,input_l))
    
py.plot(time_ord,'r',label = "ordinary method")
py.plot(time_rec,'b',label = "recursive method")
py.legend()
py.show()
'''
#Lab_Exercise_2
class Personal_info:
    def __init__(self,name,address,age,phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone
    def access_info(self):
        self_intro = "I am {} from {} and {} years old. \nFeel free to call at: {}".format(self.name,self.address,self.age,self.phone)
        return self_intro
p1 = Personal_info('Dashan Wang','Chongqing','20','1872')
p2 = Personal_info('Eric Ling','Anhui','20','3672')
p3 = Personal_info('Alan Mei','Beijing','20','161')

print(p1.access_info())
print(p2.access_info())
print(p3.access_info())

#Lab_Exercise_3
class Car:
    def __init__(self,year_model,brand,speed):
        self.__year_model = year_model
        self.__brand = brand
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
        return self.__speed
    def brake(self):
        self.__speed -= 5
        return self.__speed
    def get_speed(self):
        return self.__speed
def main():
    mycar = Car('2017','Benz',0)
    for i in range(5):
        mycar.__accelerate()
        print("The current speed is {}".format(get_speed))
    for i in range(5):
        mycar.__brake()
        print("The current speed is {}".format(get_speed))
        
        


    
    
    
    
    
    