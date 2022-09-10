# program to find grade and average
s1=int(input("enter the marks of first subject"))
s2=int(input("enter the marks of second subject"))
s3=int(input("enter the marks of third subject"))
s4=int(input("enter the marks of fourth subject"))
s5=int(input("enter the marks of fifth subject"))
avg= (s1+s2+s3+s4+s5)/5
if (avg>=90):
    print("grade:S")
elif (avg<=90)&(avg>=80):
    print("grade:A")
elif (avg<=80)&(avg>=70):
    print("grade:B")
elif (avg<=70)&(avg>=60):
    print("grade:C")
elif (avg<=60)&(avg>=50):
    print("grade:D")
else:
    print("grade:F")
