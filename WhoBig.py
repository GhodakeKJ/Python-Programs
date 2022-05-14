#Program Accepting Three values from keyboard and find biggest among them
#WhoBig.py
print("X"*50)
a=int(input("Enter The First Value :"))
b=int(input("Enter The Second Value :"))
c=int(input("Enter The Third Value :"))
print("X"*50)
if(a==b)and(b==c):
    print("All Values Are Equal/Same")
else:
    if(a>b)and(a>c):
        print("({},{},{}) Value Is Big :{}".format(a,b,c,a))
    else:
        if(b>a)and(b>c):
            print("({},{},{}) Value Is Big :{}".format(a,b,c,b))
        else:
            print("({},{},{}) Value Is Big :{}".format(a,b,c,c))
print("X"*50)