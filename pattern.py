n=int(input("enter the no of rows"))
for i in range(n):
    ch=chr(65+i)
    for j in range(i+1):
        print(ch,end="\t")
    print()
