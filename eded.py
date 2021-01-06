# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:48:34 2020

@author: Rashid Hashimzade
"""

teklik =[ [1,"bir"],[2,"iki"],[3,"üç"],[4,"dörd"],[5,"beş"],[6,"altı"],[7,"yeddi"],[8,"səkkiz"],[9,"doqquz"]]
onluq = [[10,"on"],[20,"iyirmi"], [30,"otuz"],[40,"qırx"],[50,"əlli"],[60,"altmış"], [70,"yetmiş"],[80,"səksən"],[ 90,"doksan"]]
yuzluk = [[100,"yüz"],[200,"iki yüz"],[300,"üç yüz"],[400,"dörd yüz"],[500,"beş yüz"],[600,"altı yüz"],[700,"yeddi yüz"],[800,"səkkiz yüz"],[900,"doqquz yüz"]]
minlik = [[1000,"min"],[2000,"iki min"],[3000,"üç min"],[4000," dörd min"],[5000,"beş min"],[6000,"altı min"],[7000,"yeddi min"],[8000,"səkkiz min"],[9000,"doqquz min"],]
eded = []


give = input("enter a number : ")
giveint = int(give)


if (len(give) == 1):
    for number in teklik :
        if(giveint == number[0]) :
            eded.append(number[1]) 
            

if (len(give) == 2):
    kesr = giveint%10
    tam = giveint - kesr
    for onluq1 in onluq :
        if(tam == onluq1[0]) :
           eded.append(onluq1[1])    
    if (kesr > 0):
      for number in teklik :
          if(kesr == number[0]) :
             eded.append(number[1]) 


if(len(give) == 3) : 
  kesr1 = giveint%100 #qalıq onluq
  tam1 = giveint - kesr1 #yuzluk
  kesr2 = kesr1%10 #qaliq teklik
  tam2 = kesr1 - kesr2 #onluq
  for yuz in yuzluk :
      if(tam1 == yuz[0]) :
         eded.append(yuz[1])
  if(kesr1 > 0) :
       for onluq1 in onluq :
         if(tam2 == onluq1[0]) :
           eded.append(onluq1[1])  
  if(kesr2 > 0) :
       for number in teklik :
          if(kesr2 == number[0]) :
             eded.append(number[1]) 
             
if(len(give) == 4) :
    kesr3 = giveint%1000 
    tam3 = giveint - kesr3 
    kesr4 = kesr3%100 
    tam4 = kesr3 - kesr4 
    kesr5 = kesr4%10 
    tam5 = kesr4-kesr5 
    for min1 in minlik :
        if(tam3 == min1[0]) :
           eded.append(min1[1])
    if(kesr3 > 0) :
       for yuz in yuzluk :
         if(tam4 == yuz[0]) :
            eded.append(yuz[1])
    if(kesr4 > 0) :
       for onluq1 in onluq :
         if(tam5 == onluq1[0]) :
           eded.append(onluq1[1])  
    if(kesr5 > 0 ) :
        for number in teklik :
          if(kesr5 == number[0]) :
             eded.append(number[1])
             
             
        
yazi = ""
for s in eded:
    yazi = yazi + " " + s

print(yazi)
 

if(len(give) > 4) :
   print("Error")   
    
    
    
    
    
    
    
    
