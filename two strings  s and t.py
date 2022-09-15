s1=str(input("enter the string 1:"))
s2=str(input("enter the string 2:"))
g=[]
h=[]
for i in s1:
 if i not in g:
   g.append(s1.index(i))
for k in s2:
 if k not in h:
   h.append(s2.index(k))
 if g==h:
   print("true")
else:
   print("false")

