# Gives three inputs from keyboard and Displays Which will be Big Among Them
#By if...else condition
#Three33.py
print("*"*70)
a=int(input("Enter Your First Value :"))
b=int(input("Enter Your Second Value :"))
c=int(input("Enter Your Third Value :"))
print("*"*70)
if(a==b)and(a==c):
    print("All Values Are Same/Equals...!")
else:
    if(a>b)and(a>c):print("({},{},{}) Value Is Big={}".format(a,b,c,a))
    else:
        if(b>a)and(b>c):print("({},{},{}) Value Is Big={}".format(a,b,c,b))
        else:print("({},{},{})={} Value Is Big".format(a,b,c,c))
        print("*" * 70)
print("Program Execution Is Successfull...!")
print("*"*70)