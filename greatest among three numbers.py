# program to find greatest among three numbers
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if (a>b)&(a>c):
    print("a is the greatest among three numbers")
elif (b>a)&(b>c):
    print("b is the greatest among three numbers")
else:
    print("c is the greatest among three numbers")
