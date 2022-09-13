print("Enter a: ")
a= int(input())
print("Enter b: ")
b= int(input())

a = str(a)
b = str(b)
iSum = int(a, 2) + int(b, 2)
bSum = bin(iSum)

print("Result = " + bSum)
