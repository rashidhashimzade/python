# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:32:49 2020

@author: Rashid Hashimzade
"""
sual1 = input("Nece sagird gireceksiniz? ")
sual = int (sual1)

melumatlar = []

for say in range(sual):
    s_melumatlar = input(str(say+1) + " Sargid haqqinda melumatlari girin : ")
    s_melumatlar1 = s_melumatlar.split(",")
    melumatlar.append(s_melumatlar1)
    

print(melumatlar)


sutun = input("axtarilan sutun : ")

tapdim = False
tapilanlar = []
if(sutun == "sinif") :
    sinif = input (" Sagirdin sinifini daxil edin : ")
    for melumat in melumatlar :
           if (sinif == melumat[3]):
               tapilanlar.append(melumat)
               tapdim = True

if(sutun == "ata adi") :
    ata_adi = input (" Sagirdin atasinin adini daxil edin  : ")
    for melumat in melumatlar :
           if (ata_adi == melumat[2]):
               tapilanlar.append(melumat)
               tapdim = True
               
               
if(sutun == "soyad") :
    soy_ad = input (" Sagirdin soy adini daxil edin  : ")
    for melumat in melumatlar :
           if (soy_ad == melumat[1]):
               tapilanlar.append(melumat)
               tapdim = True
               

if(sutun == "ad") :
    ad = input (" Sagirdin adini daxil edin  : ")
    for melumat in melumatlar :
           if (ad == melumat[0]):
               tapilanlar.append(melumat)
               tapdim = True
               
if (tapdim == False):
    print("sagird tapiulmadi")
else:          
    print(tapilanlar)




