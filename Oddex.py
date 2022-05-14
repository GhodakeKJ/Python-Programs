#Program For Demontrating Nth no and Displays Odd Numbers No Must be +ve By for Loop Statements
#Oddex.py
print("="*50)
n=int(input("Enter A Number :"))
if(n<=0):
    print("=" * 50)
    print("\t{} Is Invalid Input Enter +ve Number!".format(n))
    print("=" * 50)
else:
    print("-" * 50)
    print("\t Odd Numbers Within {}".format(n))
    print("-" * 50)
    i=0
    for i in range(1,n+1,2):
        print("\t\t{}".format(i))
    else:
        print("=" * 50)
