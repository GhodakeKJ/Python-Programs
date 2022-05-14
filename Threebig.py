# Write The Program Which Will be Display from three input values from keyboard and which will big among them
print("X"*50)
x=int(input("ENTER THE FIRST VALUE :"))
y=int(input("ENTER THE SECOND VALUE :"))
z=int(input("ENTER THE THIRD VALUE :"))
print("X"*50)
if(x==y)and(y==z):
    print("ALL VALUES ARE SAME")
else:
    if(x>y)and(x>y):
        print("({},{},{}) VALUE IS BIG :{}".format(x,y,z,x))
    else:
        if(y>x)and(y>z):
            print("({},{},{} VALUE IS BIG :{}".format(x,y,z,y))
        else:
            print("({},{},{}) VALUE IS BIG :{}".format(x,y,z,z))
print("X"*50)