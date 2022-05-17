def fun1(x,y):
    while(x<=y):
        yield x
        x=x+1

#Main Program
res=fun1(1,10)
while(True):
    try:
        print(next(res))
    except StopIteration:
        break