# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:52:36 2020

@author: Rashid hashimzade

"""

a = input ("Mallarin sayini daxil edin : ")
b = int(a)

myst = []

for num in range(b):    
    name = input(str(num+1) + " Malin adini daxil edin : ")
    price = float(input(" Malin qiymetini daxil edin : "))
    cnt = int(input(" Malin sayini daxil edin : "))
    myst.append([name, cnt, price, cnt*price])

print (myst)


max_mal = myst[0][3]
max_ad_mal = myst[0][0]
for mal in myst :
   if mal[3] > max_mal :
       max_mal = mal[3]
       max_ad_mal = mal[0]
      
print("En deyerli malim : " + max_ad_mal + " deyeri = "+str(max_mal))


satilan_name = input ("Aldigiz esyani daxil edin : ")
satilan_say = input ("Aldigiz esyanin sayini daxil edin : ")
c7 = int (satilan_say)
tapdim = False
n = 0

for mal in  myst :
  if (satilan_name == myst[n][0]):
      tapdim = True
      if (c7 < myst[0][1] ) :
          myst[n][1] = myst[n][1] - c7
          print("dogru")
      else :
           print(" Yeterli say yoxdur. ")
  n = n + 1
  
    
if (tapdim == False ) :
    print("bu maldan yoxdur. ")

print(myst)
    
