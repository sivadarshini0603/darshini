i=int(input("enter the initial amount"))
ch=int(input("enter your choice"))
if ch==1:
   print("deposit")
   a=int(input("enter your deposit amount"))
   if a>=1000:
    print("deposited sucessfully and your updated amount is",a+i)
   else:
    print("cant deposit")
elif ch==2:
   print("withdrawal")
   b=int(input("enter your withdrawal amount"))
   if b<i:
      print("withdraw sucessfully and your balance is",i-b)
   else:
      print("withdraw amount is high")
else:
   print("invalid choice")
