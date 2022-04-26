# Bytes Data Types

l1=[100,200,45,67,256]
print(l1,type(l1))

#  b=bytes(l1)  ValueError: bytes must be in range(0, 256)

list=[10,20,4,255,87,99]
print(list,type(list))
c=bytes(list)
print(c,type(c))


