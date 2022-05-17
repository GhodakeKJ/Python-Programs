print("="*50)
print("Enter The List Of Values Seperated By Space :")
lst=[float(val) for val in input().split()]
print("="*50)
print("Given Of List Number :{}".format(lst))
print("="*50)
s=0
for val in lst:
    print("\t{}".format(val))
    s=s+val
else:
    print("="*50)
    print("\t Sum ={}".format(s))
    print("\t Average =",s/len(lst))
    print("=" * 50)