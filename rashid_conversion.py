#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:57:53 2020

@author: rashid
"""
print("tn > tonne")
print("kg > kilogram")
print("gr > gram")
print("mg > milligram")
print("mmg > microgram")
print("l > litre")
print("ml > millilitre")
print("-------------------------")
print("km > kilometre")
print("m > metre")
print("sm > centimeter")
print("mm > millimetre")
print("mmm > micrometre")
print("-------------------------")
print("h > hectare")
print("are > are")
print("km2 > square kilometere")
print("km2 > square meter")
print("km2 > square centimeter")
print("-------------------------")


fr = str(input("enter convert from : "))
to = str(input("enter convert to : "))
number1 = int(input("enter digit : "))
converted = False
           #weight
#tonne
if (fr == "tn" and to =="kg"):
    print(str(number1*1000) + " kg")
    converted = True
    
if (fr == "tn" and to =="gr"):
    print(str(number1*1000000) + " gram")
    converted = True

if (fr == "tn" and to =="mg"):
    print(str(number1*1000000000) + " milligram")
    converted = True

if (fr == "tn" and to =="mmg"):
    print(str(number1*1000000000000) + " microgram")
    converted = True
    
#kg
if (fr == "kg" and to =="gr"):
    print(str(number1*1000) + " gram")
    converted = True
    
if (fr == "kg" and to =="mg"):
    print(str(number1*1000000) + " milligram")
    converted = True
    
if (fr == "kg" and to =="mmg"):
    print(str(number1*1000000000) + " microgram")
    converted = True
#mg
if (fr == "mg" and to =="mmg"):
    print(str(number1*1000) + " microgram")
    converted = True
    
           #su
#tonne
if (fr == "tn" and to =="l"):
    print(str(number1*1000) + " litre")
    converted = True
    
if (fr == "tn" and to =="ml"):
    print(str(number1*1000000) + " millilitre")
    converted = True
#l
if (fr == "l" and to =="ml"):
    print(str(number1*1000) + " millilitre")
    converted = True

         #uzunluq
#km   
if (fr == "km" and to =="m"):
    print(str(number1*1000) + " m")
    converted = True
    
if (fr == "km" and to =="sm"):
    print(str(number1*100000) + " sm")
    converted = True
    
if (fr == "km" and to =="mm"):
    print(str(number1*1000000) + " mm")
    converted = True
     
if (fr == "km" and to =="mmm"):
    print(str(number1*1000000000)+ " micrometre")
    converted = True
 
#m  
if (fr == "m" and to =="sm"):
    print(str(number1*100) + " sm")
    converted = True
    
if (fr == "m" and to =="mm"):
    print(str(number1*1000)+ " mm")
    converted = True 
    
if (fr == "m" and to =="mmm"):
    print(str(number1*1000000) + " micrometre")
    converted = True 
    
#sm
if (fr == "sm" and to =="mm"):
    print(str(number1*10) + " mm")
    converted = True 

if (fr == "sm" and to =="mmm"):
    print(str(number1*10000 )+ " micrometre")
    converted = True
    
#mm
if (fr == "mm" and to =="mmm"):
    print(str(number1*1000) + " micrometre")
    converted = True
    
#hectar
if (fr == "h" and to =="are"):
    print(str(number1*100) + " are")
    converted = True    
    
if (fr == "h" and to =="km2"):
    print(str(number1*0.01) + " kilometer squard")
    converted = True
    
if (fr == "h" and to =="m2"):
    print(str(number1*10000) + " meter square")
    converted = True

if (fr == "h" and to =="sm2"):
    print(str(number1*100000000) + " centimeter square")
    converted = True
 
#are
if (fr == "are" and to =="km2"):
    print(str(number1*0.0001) + " kilometer square")
    converted = True

if (fr == "are" and to =="m2"):
    print(str(number1*100) + " meter square")
    converted = True

if (fr == "are" and to =="sm2"):
    print(str(number1*1000000) + " centimeter square")
    converted = True
    
    
# if conversion not happened    
if (converted == False):
    print("I don't know this conversion")
    