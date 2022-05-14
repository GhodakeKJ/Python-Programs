def readvalues():
    n=int(input("Enter How Many Numbers Sum And Avg Want To Find :"))
    if(n<=0):
        print("{} Is Invalid Input..Enter +ve Numbers".format(n))
    else:
        lst=[]
        for i in range(1,n+1):
            val=int(input("Enter Value :".format(i)))
            lst.append(val)
            return lst
def findsumavg(obj):
    if(obj!=None):
        s=0
        for val in obj:
            print("\t\t {}".format(val))
            s=s+val
        else:
            print("Sum ={}".format(s))
            print("\t\t Average ={}".format(s/len(obj)))

    else:
        print("\nDont Have Any Value And Can't Find Sum And Average")

    #main Program
