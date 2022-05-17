def fun1(x,y,z):
    while(x<=y):
        yield x
        x=x+z

#Main Program
res=fun1(500,100,-50)
while(True):
    try:
        print(next(res))
    except StopIteration:
        break