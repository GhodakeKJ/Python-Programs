# For For Demonstrating Dislpyas even Numbers of Nth no n Must Be +ve by for loop
#Evenex1.py
print("="*50)
n=int(input("\tEnter A Number :"))
if(n<=0):
    print("-" * 50)
    print("\t{} Is Invalid Input Plz Enter +ve Number !".format(n))
    print("=" * 50)
else:
    print("="*50)
    print("\tEven Number Within : {}".format(n))
    print("=" * 50)
    i=1
    for i in range(2,n+1,2):
        print("\t\t{}".format(i))
    else:
        print("=" * 50)
