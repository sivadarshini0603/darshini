s=int(input("enter your salary per month"))
l=int(input("enter the leave days"))
if l<=2:
   print("the remaining salary is",s)
elif l>2:
   print("the remaining salary is",s-(l*500)+1000)
else:
   print("invalid")
