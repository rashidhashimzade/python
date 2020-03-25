#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:57:53 2020

@author: rashid
"""

fr = str(input("enter convert from : "))
to = str(input("enter convert to : "))
number1 = int(input("enter digit : "))
converted = False

#km
if (fr == "km" and to =="km"):
    print(number1 + " km")
    converted = True
    
if (fr == "km" and to =="m"):
    print(str(number1*1000) + "m")
    converted = True
    
if (fr == "km" and to =="sm"):
    print(str(number1*100000) + " sm")
    converted = True
    
if (fr == "km" and to =="mm"):
    print(str(number1*1000000 + " mm")
    converted = True
     
if (fr == "km" and to =="micrometre"):
    print(number1*1000000000 + " micrometre")
    converted = True
 
#m
if(fr == "m" and to =="m"):
    print(number1 + " m")
    converted = True
    
if (fr == "m" and to =="sm"):
    print(number1*100 + " sm")
    converted = True
    
if (fr == "m" and to =="mm"):
    print(number1*1000 + " mm")
    converted = True 
    
if (fr == "m" and to =="micrometre"):
    print(number1*1000000 + " micrometre")
    converted = True 
    
#sm
if (fr == "sm" and to =="sm"):
    print(number1 + " sm")
    converted = True 

if (fr == "sm" and to =="mm"):
    print(number1*10 + " mm")
    converted = True 

if (fr == "sm" and to =="micrometre"):
    print(number1*10000 + " micrometre")
    converted = True
    
#mm
if (fr == "mm" and to =="mm"):
    print(number1 + " mm")
    converted = True

if (fr == "mm" and to =="micrometre"):
    print(number1*1000 + " micrometre")
    converted = True
    
#micrometre
if (fr == "micrometre" and to =="micrometre"):
    print(number1 + " micrometre")
    converted = True

if (converted == False):
    print("I don't know this conversion")

    