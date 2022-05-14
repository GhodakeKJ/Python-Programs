#Membership Operators
a=float(input("Enter Your First Value a: "))
b=float(input("Enter Your Second Value b :"))
print("="*50)
print("The Original Value Of A:{}".format(a))
print("The Original Value Of B :{}".format(b))
print("="*50)
#Swapped The Values
a=a^b
b=a^b
a=a^b
#Print The Swappped Values
print("Swapped Value Of A :{}".format(a))
print("Swapped Value Of B :{}".format(b))
print("="*50)