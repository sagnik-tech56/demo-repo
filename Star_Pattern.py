z=int(input("Enter the no of rows in your pattern: "))
if z%2==1:
    for i in range((z+1)//2):
        for j in range(i):
            print(" ",end='')
        for k in range(z-2*i):
            print("*",end='')
        print()
else:
    print("Get lost or enter odd number next time")
