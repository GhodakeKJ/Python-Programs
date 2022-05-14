def show(obj):
    print("="*50)
    print("Type Of Object =",type(obj))
    print("-" * 50)
    for val in obj:
        print("\t\t{}".format(val))
def disp(obj):
    print("="*50)
    print("Type Of Object ".format(obj))
    print("-"*50)
    for k,v in obj.items():
        print("{}==========>{}".format(k,v))

#main Program
list=[10,20,30,40,50,60,70]
show(list)

tuple=(100,200,300,400,500,600,700)
show(tuple)

set={"java","Python","Data Science","Django","UI","Machine Lerning"}
show(set)

dict={1:"Karan",2:"Aniket",3:"Scott",4:"Rossum",5:"Dannish"}
disp(dict)