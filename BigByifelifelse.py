# Gives three inputs from keyboard and Displays Which will be Big Among Them
#by if..elif..else condition
#BigByifelifelse.py
print("*"*70)
a=int(input("ENTER THE FIRST VALUE :"))
b=int(input("ENTER THE SECOND VALUE :"))
c=int(input("ENTER THE THIRD VALUE :"))
print("*"*70)
if(a==b)and(b==c):
    print("ALL VALUES ARE SAME / EQUAL...!")
elif (a>b)and(a>c):
    print("({},{},{})VALUE IS BIG={}".format(a,b,c,a))
elif (b>a)and(b>c):
    print("({},{},{})VALUE IS BIG={}".format(a,b,c,b))
elif (c>a)and(c>b):
    print("({},{},{})VALUE IS BIG={}".format(a,b,c,c))
print("*" * 70)