# program to solve quadratic equaton
#import complex math module
import cmath
a=float(input("enter the value of a"))
b=float(input("enter the value of b"))
c=float(input("enter the value of c"))
d= (b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print('the solution are{0}and{1}'.format(sol1,sol2))
