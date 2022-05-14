print("enter list of values separated by comma")
lst=[ int(val)  for val in input().split()]
plst=list()
nlst=list()
for val in lst:
    if val>0:
        plst.append(val)
    elif(val<0):
        nlst.append(val)
else:
    print("given list={}".format(lst))
    print("possitive list={}".format(plst))
    print("negative list={}".format(nlst))