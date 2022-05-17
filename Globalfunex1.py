a=10
b=20  #Here a,b,c,d Are Global Variables
c=30
d=40
def fun1():
    global c,d  #Here c,d Decleard As global variables
    c=c+1
    d=d+1
    global x,y
    x=16
    y=12
    x=1+4 #Here a,b Are Local Variable
    y=y+8
    res=a+b+c+d+globals().get('a')+globals().get('b')
    print("Result =",res)


#Main Program
fun1()
print("Value Of Global a ={}".format(a))
print("Value Of Global b ={}".format(b))
print("Value Of Global c ={}".format(c))
print("Value Of Global d ={}".format(d))
print("Value Of Local x ={}".format(x))
print("Value Of Local y ={}".format(y))
