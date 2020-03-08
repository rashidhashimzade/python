import datetime
from datetime import date
name1 = "Ramin"
# FIRST PERSON
your_born_date = datetime.datetime(2007,1,1)
now = datetime.datetime.today()
day_b = now-your_born_date
print(str(name1) + " your life in days = " + str(day_b.days))
from dateutil.relativedelta import relativedelta
difference_in_years_b = relativedelta(now, your_born_date).years
print("your life in years = " + str(difference_in_years_b))
difference_in_month_b = relativedelta(now, your_born_date).months
difference_in_month_b = difference_in_years_b*12+difference_in_month_b
print("your life in month = " + str(difference_in_month_b)) 
difference_in_week_b = day_b.days/7
print("your life in week = " + str(difference_in_week_b))

# SECOND PERSON
print("----------------------------------------------")
name2 = "Rashid"

your_born_date =datetime.datetime (2010,3,8)
day_a= now-your_born_date

print(str(name2) +  " your life in days = " + str(day_a.days))
from dateutil.relativedelta import relativedelta
difference_in_years_a = relativedelta(now, your_born_date).years
print("your life in years = " + str(difference_in_years_a))
difference_in_month_a = relativedelta(now, your_born_date).months
difference_in_month_a = difference_in_years_a*12+difference_in_month_a
print("your life in month = " + str(difference_in_month_a)) 
difference_in_week_a = day_a.days/7
print("your life in week = " + str(difference_in_week_a)) 

print("----------------------------------------------")
# DIFFERENCE PERSON
if (difference_in_years_b > difference_in_years_a):
  olderPerson = name1
  youngerPerson = name2
else :
  olderPerson = name2
  youngerPerson = name1

print(youngerPerson + " is younger than " + olderPerson)

bigger= abs(day_b-day_a)
print("in days = " + str(bigger.days))

bigger = abs(difference_in_years_b-difference_in_years_a)
print("in years = " + str(bigger))

bigger = abs(difference_in_month_b-difference_in_month_a)
print("in months = " + str(bigger))

bigger = abs(difference_in_week_b-difference_in_week_a)
print("in weeks = " + str(bigger))
