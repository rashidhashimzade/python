# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:34:07 2021

@author: Rashid Hashimzade
"""

teklik =[ [1,"bir"],[2,"iki"],[3,"üç"],[4,"dörd"],[5,"beş"],[6,"altı"],[7,"yeddi"],[8,"səkkiz"],[9,"doqquz"]]
onluq = [[10,"on"],[20,"iyirmi"], [30,"otuz"],[40,"qırx"],[50,"əlli"],[60,"altmış"], [70,"yetmiş"],[80,"səksən"],[ 90,"doksan"]]
eded = []


def teklikTap(a):
    for number in teklik :
        if(a == number[0]) :
            return number[1]
        
def onluqTap(a):
    for number in onluq :
        if(a == number[0]) :
            return number[1]        

give = input("enter a number : ")
giveint = int(give)


if (len(give) == 1):
    eded.append(teklikTap(giveint))
            

if (len(give) == 2):
    kesr = giveint%10
    tam = giveint - kesr
    for onluq1 in onluq :
        if(tam == onluq1[0]) :
           eded.append(onluq1[1])    
    if (kesr > 0):
        eded.append(teklikTap(kesr))


if(len(give) == 3) : 
    kesr1 = giveint%100 #qalıq onluq
    tam1 = giveint - kesr1 #yuzluk
    yuzluk = tam1/100
    eded.append((teklikTap(yuzluk) + " yuz"))
    
    kesr2 = kesr1%10 #qaliq teklik
    tam2 = kesr1 - kesr2 #onluq
    eded.append(onluqTap(tam2))
    
    eded.append(teklikTap(kesr2))
    
if(len(give) == 4) :    
    kesr1 = giveint%1000 #qalıq onluq
    tam1 = giveint - kesr1 #minlik
    minlik = tam1/1000
    eded.append((teklikTap(minlik) + " min"))
    
    kesr2 = kesr1%100 #qaliq yuzluk
    tam2 = kesr1 - kesr2 #yuzluk
    tam2_teklik = tam2/100 #yuzluyun teki
    eded.append(teklikTap(tam2_teklik) + " yuz")
    
    kesr3 = kesr2%10 #qaliq onluq
    tam3 = kesr2 - kesr3 #onluq
    eded.append(onluqTap(tam3))
    
    eded.append(teklikTap(kesr3))    
    
                
  
  
  

yazi = ""
for s in eded:
    yazi = yazi + " " + s

print(yazi)