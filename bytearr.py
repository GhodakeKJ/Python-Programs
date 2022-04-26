# Some practice examples on bytearray data type

l1=[3,244,10,3,155,255,133,6,67,80]
ba=bytearray(l1)
print(ba,type(ba))
print(ba[5])

for k in ba:
    print(k)