#Addex.py
print("="*50)
n=int(input("Enter A Number :"))
if(n<=0):
    print("-" * 50)
    print("{} is invalid input ... Enter +ve Number !".format(n))
    print("-" * 50)
else:
    i=1
    s=1
    while(i<=n):
        print("{}\t+\t{}\t=\t{}".format(i,s,i+s))
        i=i+1
    else:
        print()
        print("=" * 50)