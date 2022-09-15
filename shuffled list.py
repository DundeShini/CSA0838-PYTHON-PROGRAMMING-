si=[]
sk=[]
ns1=int(input("enter 11 range:"))
for i in range (ns1):
    i=int(input("enter:"))
    si.append(i)
ns2=int(input("enter the 12 range:"))
for k in range(ns2):
    k=int(input("enter:"))
    sk.append(k)
s=[]
s=si+sk
s.sort()
print("List:",s)
