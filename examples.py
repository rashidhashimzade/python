##############################################################################
# input istifade qaydasi

name = input("what is your quest?")
print ("your  quest is " + name + "." )
print(type(name))


f1 = input("first digit : ")
f2 = input("second digit : ")
total = float(f1) +float(f2)
print(total)


##############################################################################
# parse string : string bolunmesi qaydasi
to_slice = "Just do it!"
print(to_slice[10])   # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])   # prints "it!"
print(to_slice[:4])   # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"


##############################################################################
# Asterisk triangle
print("*******\n ***** \n  ***  \n   *   ")
print("   *   \n  ***  \n ***** \n*******")


##############################################################################
# int() how to use


#solution 1
abc = int(input("please enter  the integer."))
print("your integer is " + str(abc+10))
print (type (abc))


#solution 2
use_int = input("Please enter an integer.")
 
print(int(use_int) + 10)
  
##############################################################################

#functions

def milesToMeters(mil):
    metr = mil * 1600
    return metr
    
mil = int(input("enter miles : "))
print(str(milesToMeters(mil)) + "meter")


mil2 = int(input("enter miles second time : "))
print(str(milesToMeters(mil2)) + "meter")


###############################################################################
import random
from random import randint

print (randint(1,10))
###############################################################################
#intro to flow control


number1 = int(input("enter first digit : "))
number2 = int(input("enter second digit : "))


if (number1<number2 ) :
   print ("number2 bigger than number1 for " + str (number2-number1) + " times.")
else :
   print("number1 bigger than number2 for " + str(number1-number2) + " times.")
   
   
a = "rasid"
b = (a != "Rasid") 
c = (a == "Rasid") 
print("b =" +  str(b))
print("c =" +  str(c))
   
   
a = 1
while(a < 11):
    print("inside")
    a = a + 1
print("outside")


###################################################################3
# VARIABLE SCOPE
fruit = "armud"  

def myFunction():
    fruit = "apple"
    print(fruit)

myFunction()
print(fruit)











