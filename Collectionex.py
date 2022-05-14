def display(obj):
    print("="*50)
    print("Type Of Object =",type(obj))
    print("="*50)
    for val in obj:
        print("\t\t {}".format(val))
def show (obj):
    print("=" * 50)
    print("Type Of Object =", type(obj))
    print("=" * 50)
    for x,y in obj.items():
        print("\t\t {}===========>{}".format(x,y))


#Main Program
list=[10,20,30,40,50,60,70,80,90,100]
display(list)  #Funcation Call
tuple=("Python",10,True,78.80,"Django","Rossum")
display(tuple)
set={44,22,76,98,356,86,122,644,865}
display(set)
dict={1:"Rossum",2:"Dannish",3:"KVR",4:"Eienstin",5:"Scott"}
show(dict)
print("=" * 50)
