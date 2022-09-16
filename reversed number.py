My_Number = int(input("Please provide the number to be reversed: "))
reversed_Number = 0
while(My_Number > 0):
 Reminder = My_Number %10
 reversed_Number = (reversed_Number *10) + Reminder
 My_Number = My_Number //10
print("reversed of the provided number is = %d" %reversed_Number)
