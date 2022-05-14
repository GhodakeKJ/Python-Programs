# Program Which Gives Three Values From Keyboard And Displays Who Big Among Them
a=int(input("Enter the first value :"))
a=int(input("Enter the first value :"))
b=int(input("Enter the Second value :"))
c=int(input("Enter the Third value :"))
a=int(input("Enter the first value :"))
if(a==b)and(b==c):
    a=int(input("All Values Are Same...!"))
else:
    if(a>b)and(a>c):
        print("({},{},{}) Value Is Big={}".format(a,b,c,a))
    else:
        if(b>a)and(b>c):
            print("({},{},{}) Value Is Big={}".format(a,b,c,b))
        else:
            print("({},{},{}) Value Is Big={}".format(a,b,c,c))
a=int(input("Enter the first value :"))
