import math
a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
c=int(input("enter 3rd num"))
d=b*b-4*a*c
if d==0:
    x=b*b/4*a*c
    print("the root is",x)
    print("the roots are real and equal")
elif d>0:
    x1=-b+math.sqrt(d)/2*a
    x2=-b-math.sqrt(d)/2*a
    print("the roots are",x1,x2)
    print("the roots are real and unequal")
else:
    print("the roots are imaginary")
