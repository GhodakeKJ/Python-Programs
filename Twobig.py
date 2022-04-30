a=int(input("Enter First Value :"))
b=int(input("Enter Second Value :"))
c=int(input("Enter Third Value :"))
if(a==b)and(a==c):
    print("All Values Are Equals ")
elif (a>b)and(a>c):
    print("({},{},{}) Value Is Big={}".format(a,b,c,a))
elif (b>a)and(b>c):
    print("({},{},{}) Value Is Big ={}".format(a,b,c,b))
elif (c>a)and(c>b):
    print("({},{},{}) Value Is Big ={}".format(a,b,c,c))
else:
    print("Program Execution Successfull")
