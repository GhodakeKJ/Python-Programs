l1=[10,20,30,40,50,60,20,40,60]
print(l1,type(l1),id(l1))
l2=l1
print(l2,type(l2),id(l2))
l1.insert(1,"Python")
l2.append("Django")
print(l2,type(l2),id(l2))
print(l1,type(l1),id(l1))
l1.reverse()
print(l1,type(l1),id(l1))
l1.count(40)
print(l1,type(l1),id(l1))