def addop():
    p=int(input("Enter First Value :"))
    q=int(input("Enter Second Value :"))
    r=p+q
    return p,q,r

#Main Program
a,b,result=addop()
print("Sum Of ({} and {}) = {}".format(a,b,result))
res=addop()
print("Sum = ({} and {}) = {}".format(res[0],res[1],res[2]))