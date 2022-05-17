def fun1(k,v,r):
    while(k<=v):
        yield k
        k=k+r


#Main Program
res=fun1(1,10,1)
while(True):
    try:
        print(next(res))
    except StopIteration:
        break