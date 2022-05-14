print("Enter The Number Of List Seperated By Space :")
lst=[ int(val) for val in input().split() ]
print("="*50)
#Create Empty List
newlst=[]
for val in lst:
    newlst.append(val)
    print("New List =",newlst)
    print("="*50)
    print("==================OR=========================")
    newlst=[ val**2  for val in lst]
    print("New List =",newlst)