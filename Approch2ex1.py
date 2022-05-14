def addop(x,y):
    z=x+y
    return z
x=int(input("Enter First Value :"))
y=int(input("Enter Second Value :"))
result=addop(x,y)
print("Sum ({} and {}) = {}".format(x,y,result))