l1=[10,20,30,40,50,60]
print(l1,type(l1),id(l1))
l1.append(10)
l1.append(70)
l1.append(30)
print(l1,type(l1),id(l1))
l1.insert(1,"Karan")
print(l1)
l1.remove(30)
print(l1)
l1.remove(10)
l1.remove(10)
print(l1)
l1.pop(6)
print(l1)
l1.pop()
l1.pop()
print(l1,id(l1))
l2=l1.copy()
print(l2,type(l2),id(l2))
l2.append("Python")
l1.insert(1,"Django")
print(l1,type(l1),id(l1))
print(l2,type(l2),id(l2))
