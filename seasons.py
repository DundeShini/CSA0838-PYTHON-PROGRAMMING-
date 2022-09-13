#program to display season

month=input("enter a month")
date=int(input("enter the date"))
if(date>0 and date<=31):
    if(month=='april' or month=='may'):
         print("summer")
    if(month=='june' and date<=20):
         print("summer")
    if(month=='march' and date>20):
         print("summer")
    if(month=='june' and date>20):
         print("spring")
    if(month=='july'or month=='august'):
         print("spring")
    if(month=='september' and date<=20):
         print("spring")
    if(month=='september' and date>20):
         print("fall")
    if(month=='october' or month=='november'):
         print("fall")
    if(month=='december' and date<=20):
         print("fall")
    if(month=='january' or month=='february'):
         print("winter")
    if(month=='march' and date<=20):
         print("winter")
    if(month=='december' and date>20):
        print("winter")

else:
    print("enter valid input")
