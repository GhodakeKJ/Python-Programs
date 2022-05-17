def fun1(x,y,z):
    while(x<=y):
        yield x
        x=x+z

#Main Program
res=fun1(0,500,50)
while(True):
    try:
        print(next(res))
    except StopIteration:
        break