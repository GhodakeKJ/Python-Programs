n=int(input("Enter Your Value :"))
print("*"*60)
if(n==0):
    print("{} Value Is Zero".format(n))
else:
    if(n>0):
        print("{} Value Is Potive".format(n))
    else:
        if(n<0):
            print("{} Value Is Negative".format(n))
            print("*" * 60)
print("Program Execution Is Successfull...!")
print("*"*60)