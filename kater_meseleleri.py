# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:24:03 2020

@author: Rashid Hashimzade

"""

sual = input("Sualda sizden ne istenilir?")


if(sual == "kv") :
    time1 = input("Vaxti daxil edin. ")
    time = int(time1)
    direction = input("Istiqameti daxil edin : ")
    vr1 = input("Cayin suretini daxil edin. ")
    vr = int(vr1)
    yol1 = input("Cemi gedilen yolu daxil edin : ")
    yol = int(yol1)
    
    if(direction == "rs") :
      print(int((yol+time*vr)/time))
    if(direction == "ros") :
      print(int((yol-time*vr)/time))
      
      
      
      
if(sual == "t") :
    direction = input("Istiqameti daxil edin : ")
    vr1 = input("Cayin suretini daxil edin. ")
    vr = int(vr1)
    yol1 = input("Cemi gedilen yolu daxil edin : ")
    yol = int(yol1)
    suret1 = input("Katerin suretini daxil edin : ")
    suret = int(suret1)
     
    
    if(direction == "rs") :
      print(int(yol/(suret+vr)))
    if(direction == "ros") :
      print(int(yol/(suret-vr)))

if(sual == "rv") :
    time1 = input("Vaxti daxil edin. ")
    time = int(time1)
    direction = input("Istiqameti daxil edin : ")
    yol1 = input("Cemi gedilen yolu daxil edin : ")
    yol = int(yol1)
    suret1 = input("Katerin suretini daxil edin : ")
    suret = int(suret1)
    
    
    if(direction == "rs") :
      print(int((time*suret-yol)/time))
    if(direction == "ros") :
      print(int(abs((yol-(time*suret))/time)))


if(sual == "dis") :
    time1 = input("Vaxti daxil edin. ")
    time = int(time1)
    direction = input("Istiqameti daxil edin : ")
    suret1 = input("Katerin suretini daxil edin : ")
    suret = int(suret1)
    vr1 = input("Cayin suretini daxil edin : ")
    vr = int(vr1)
    
    
    if(direction == "rs") :
      print(int(time*(suret+vr)))
    if(direction == "ros") :
      print(int(time*(suret-vr)))





      
      
      
      
      
      
      
      
