#Program For Accepting List Of names From KBD And Sort The Name
#SortName1.py
def readname():
    print("Enter Names Of People :")
    lst=[str(val) for val in input().split() ]
    return lst
def sortname(obj):
    if(len(obj)==0):
        print("No Need To Sort Any Thing,Bcoz List Does Not Contain Any Name :")
    else:
        print("="*50)
        print("List Of Names In Original Order :")
        print("="*50)
        for val in obj:
            print("\t {} ".format(val))
            obj.sort()
            #Acending Order
            print("List Of Names In Acending Order :")
            print("="*50)
            for val in obj:
                print("\t {}".format(val))
                obj.sort(reverse=True) #Decending Order
                print("List Of Names In Decending Order :")
                print("="*50)
                for val in obj:
                    print("\t {}".format(val))
    #       Main Program
    lst=readname() #Function Call
    sortname(lst)