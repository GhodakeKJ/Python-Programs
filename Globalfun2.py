def fun1():
    d=globals()
    print("Type of d=",type(d))  #Type of d= <class 'dict'>
    for k,v in d.items():
        print("{} --------->> \t{}".format(k,v))
        print("Programmer Definened Global Variable")
        print("Value Of a ===>",d['a'])
        print("Value Of b ===>", d['b'])
        print("Value Of c ===>", d['c'])

#Main Program
a=200
b=350
c=4589
fun1()