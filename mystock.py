# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:08:59 2020

@author: Rashid
"""

# malin girisi
a = input (" Mallarin sayini daxil edin : ")
b = int (a)

# sayi deyeri ve adi daxil edirik.

myst = []

for num in range(b):    
    name = input(str(num+1) + " Malin adini daxil edin : ")
    price = float(input(" Malin qiymetini daxil edin : "))
    cnt = int(input(" Malin sayini daxil edin : "))
    myst.append([name, cnt, price, cnt*price])

    
print (myst)


# en boyuk deyeri tapiram

max_mal = myst[0][3]
max_ad_mal = myst[0][0]
for mal in myst :
    if mal[3] > max_mal :
        max_mal = mal[3]
        max_ad_mal = mal[0]
        
print("En deyerli malim : " + max_ad_mal + " deyeri = "+str(max_mal))
   
    

#satiram
satilan_name = input ("Aldigiz esyani daxil edin : ")
satilan_say = input ("Aldigiz esyanin sayini daxil edin : ")
c7 = int (satilan_say)
tapdim = False

for mal in  myst :
  if (satilan_name == myst[0][0] ):
      tapdim = True
      print("dogru") 
      if (c7 < myst[0][3] ):
          tapdim = True
          print("dogru")
      
if (tapdim == False ) :
    print("bu maldan yoxdur. ")
    