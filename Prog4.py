#Prog4.py
# Program Which Displays Variable Length Arguments by Using Find The Sum Of Numbers

def show(sname,*nums,s=0):
	print("="*50)
	print("\tStudent Name :{}".format(sname))
	for val in nums:
		print("{}".format(val))
		s=s+val
	print()
	print("\tSum :{}".format(s))
	print("="*50)


#Main Program
show("Rossum",10,20,30)
show("Rossum",10,20,3090,4652,235)