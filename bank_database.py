# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:07:06 2020

@author: Rashid Hashimzade
"""

sual1 = input("how many account will you enter : ")
sual = int(sual1)


abc = []


for say in range(sual):
    account_name  = input(str(say+1) + " Enter account name : ")
    account_num = input("Enter account number : ")
    money1 = input(" Enter your cash : ")
    money = float(money1)
    
    abc.append([account_num,account_name, money])
   
    
print(abc)




operation = input(" Which operation do you want to do : ")
n = 0


if(operation == "kocurme") :
    ac1 = input("Enter the number of account that you want to take money from : ")
    ac2 = input("Enter the number of account that you want to send money to : ")
    amt = float(input("Amount : "))
    for num in abc :
       if (ac1 == num[0]) :
           if (num[2] < amt ) :
               print("ERROR!")
               break
           abc[n][2] = abc[n][2] - amt
       elif(ac2 == num[0]) :
           abc[n][2] = abc[n][2] + amt            
       n = n + 1

print(abc)




if(operation == "axtaris"):
    axtar = input("Enter search criteria: ")

    if(axtar == "nomre") :
        acc_num  = input ("enter account number : ")
    if(axtar == "accountin adi ") :
        acc_name = input ("Enter account name : ")    
    
        
    tapdim = False    
    for melumat in abc :
        if(axtar == "nomre") and (acc_num == melumat[0]):
            print(melumat)
            tapdim = True
            break
        if(axtar == "accountin adi ") and (acc_name == melumat[1]):
            print(melumat)
            tapdim = True
            break               
    
    if (tapdim == False):
       print("Tapilmadi")
               
