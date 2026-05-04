temp=input("enter the temparature")
humi=input("enter the humidity")
if temp=="warm":
    if humi=="dry":
        print("play basketball")
    elif humi=="humid":
        print("play tennis")
    else:
        print("invalid")
if temp=="cold":
    if humi=="dry":
        print("play cricket")
    elif humi=="humid":
        print("play swim")
    else:
        print("invalid")
