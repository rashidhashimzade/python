import datetime
name = "Ramin"
# FIRST PERSON
your_born_date =datetime.datetime (2007,1,1)
now = datetime.datetime(2020,3,8)
day_b = now-your_born_date
print(str(name) + " your life in days = " + str(day_b.days))
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
name = "Elmira"

your_born_date =datetime.datetime (1960,5,16)
day_a= now-your_born_date

print(str(name) +  " your life in days = " + str(day_a.days))
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
bigger= abs(day_b-day_a)
print("your life bigger in days = " + str(bigger.days))

bigger = abs(difference_in_years_b-difference_in_years_a)
print("your life bigger in year = " + str(bigger))

bigger = abs(difference_in_month_b-difference_in_month_a)
print("your life bigger in month = " + str(bigger))

bigger = abs(difference_in_week_b-difference_in_week_a)
print("your life bigger in week = " + str(bigger))
