n=float(input("enter the number of new louves ordered"))
o=float(input("enter the number of old louves ordered"))
r=185
re="{:.2f}".format(r)
print("the regular price for the new loaf is ",re)
he=185*n
hm="{:.2f}".format(he)
print("the total price for the new loaf is ", hm)
h=185*0.6
oh=h*o
ohh="{:.2f}".format(oh)
print("the total price for the old loaf is ",ohh)
print("total is :")
total=oh+he
to="{:.2f}".format(total)
print(to)
