# Some Basics Examples On List Categary data type


l1=[10,344,50,24,4356,5675,2345]
print(l1,type(l1))
l1.append("Python")
l1.append("KVR")
l1.append("Django")
print(l1,type(l1),id(l1))
print(len(l1))

l1.insert(1,"Karan")
l1.insert(0,"Guido Van Rossum")
print(l1,type(l1),id(l1))

l1.pop(0)
l1.pop(3)
print(l1,type(l1),id(l1))

l1.remove("Karan")
l1.remove("KVR")
l1.remove(24)

del l1[3]
del l1[2]
print(l1,type(l1),id(l1))

# Some Examples Of Shallo Copy
print(l1,id(l1))
l2=l1.copy()
l1.append("Karan")
l1.insert(1,"Python")
print(l2,type(l2),id(l2))
print(l1,type(l1),id(l1))

print("*"*50)
l4=l1
print(l4,type(l4),id(l4))
print(l1,type(l1),id(l1))
print("*"*50)
l4.append("Ritche")
l4.insert(1,"Django")
print(l4,type(l4),id(l4))
print(l1,type(l1),id(l1))
l4.index[10]
print(l4,type(l4),id(l4))
print(l1,type(l1),id(l1))
print("*"*50)