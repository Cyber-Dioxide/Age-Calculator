import os
import sys,time,random
from colorama import Fore
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
all_col = [red,green,orange,cyan,lightgrey,lightred,lightgreen,yellow,lightcyan]
ran = random.choice(all_col)
os.system("clear")
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(4./90)

sprint(ran+"-"*30)



print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)

name = input(ran+"Enter you name: ")
date = int(input(ran+"\nEnter the date of birth from 1 - 31: "))
month = int(input(ran+"\nEnter the number of month from 1 - 12: "))
year = int(input(ran+"\nEnter the year name on which you were born! Like i was born in 1999: "))
gender = input(ran+"\nEnter you gender \"M\" for male \"F\" for female: ")




sprint("We are setting up thingz for you")

list_for_male = ['m','M','male','Male']
list_for_female = ['f','F','Female','female']


if gender in list_for_female:
    print(ran,"\nMrs.", name ,"you are born in" ,date, month, year )
elif gender in list_for_male:
    print(ran,"\nMr." , name , "you are born in",date, month, year)
else:
    if gender not in list_for_male or list_for_female:
        print(ran, name , "You are born in" ,date,month,year )



sprint(ran+"-"*10)
sprint(ran+"\nLet me calculate some more intresting things about you")
sprint(ran+"\ncalculating days...")
sprint(ran+"\ncalculating seconds...")
sprint(ran+"\ncalculatinng minutes...")
sprint(ran+"\ncalulating hours...")
sprint(ran+"\ncalculating......")

import datetime


current_year = datetime.date.today().year
age_month = datetime.date.today().month
age_day = datetime.date.today().day


leap=0
for i in range(year,2021+1):
	if i%4==0:
		leap=leap+1
if year%4==0 and month<3:
	leap = leap - 1

age = current_year - year
total_months = abs(age_month - month)
total_days = abs(age_day - date)

months=(age*12)+age_month
days=(age*365)+leap+(age_day)
hour= (age*365*24)+(leap*24)+(age_day*24)
mins= (age*365*24*60)+(leap*24*60)+(age_day*24*60)
secs= (age*365*24*60*60)+(leap*24*60*60)+(age_day*24*60*60)


print(ran+"The time you have spent on Earth",age,"in years,",months,"in months,",days,"in days,",hour,"in hours,",mins,"in minutes and",secs,"in seconds.")


sprint(ran+"-----------------------------------------")
sprint(ran+"Have a good day")





































