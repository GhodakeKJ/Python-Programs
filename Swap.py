# Write The Program For Swapping Two Values By XOR
print("="*60)
a=int(input("Enter Your Value a :"))
b=int(input("Enter Your Value b:"))
# Print Original Values Of a And b
print("="*60)
print("Original Value Of a={}".format(a))
print("Original Value Of b={}".format(b))
print("="*60)
# Swapped The Values
a=a^b
b=a^b
a=a^b
#print The Swapped Values
print("="*60)
print("Swapped Values Of a ={}".format(a))
print("Swapped Values Of b ={} ".format(b))
print("="*60)