#Programing For Demonstrating Sum By For Loop Statements Nth no Must be +ve
#Sumex.py
print("="*50)
n=int(input("Enter A Number :"))
if(n<=0):
    print("-" * 50)
    print("{} Is Invalid Input...! Enter +ve Number".format(n))
    print("-" * 50)
else:
    s=0
    ss=0
    cs=0
    print("="*50)
    print("Sum Of Numbers Within :{}".format(n))
    print("=" * 50)

    for i in range(1,n+1):
        print("\t{} \t\t{} \t\t{}".format(i,i*2,i*3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("=" * 50)
        print("\t{}\t\t{}\t\t{}".format(s,ss,cs))
        print("=" * 50)

