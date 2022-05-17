a=100
b=200
c=300

def fun1():
    d=globals()
    print("Type Of d =",type(d))
    for k,v in d.items():
        print("\t ====> \t{}".format(k,v))
        print("Programmer Defined Global Variable Way-1")
        print("Value Of a = {}".format(globals().get('a')))
        print("Value Of b = {}".format(globals().get('b')))
        print("Value Of c = {}".format(globals().get('c')))
        print("=======================================================")
        print("Programmer Defined Global Variable Way-2")
        print("Value Of a = ",d['a'])
        print("Value Of b = ",d['b'])
        print("Value Of c = ",d['c'])
        print("=======================================================")
        print("Programmer Defined Global Variable Way-3")
        print("Value Of a = ", d.get('a'))
        print("Value Of b = ", d.get('b'))
        print("Value Of c = ", d.get('c'))


#Main Program
fun1()