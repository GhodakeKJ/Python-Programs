#Bytes.py
x=[10,20,30,40,50,60,70]
b1=bytes(x)
print(b1,type(b1))

print(b1[0])
print(b1[1])
print(b1[5])
print(b1[6])
for i in b1:
	print(i)

z=(10,20,30,40,50,60,70,80,90,100,200)
b=bytes(z)
print(b,type(b))
for s in b:
	print(s)