#Prog2.py
# Program Which Displays Variable Length Arguments
def display(sid,sname,*detail):
	print("="*50)
	print("\tStudent Id={}".format(sid))
	print("\tStudent Name={}".format(sname))
	print("\tStudent Details Of ={}".format(sname))
	for val in detail:
		print("\t\t",val)
	print("="*50)
	


#Main Program
display(111,"Kinney",10,20,30,"English",77.99,"Django")
display(222,"Robert",True)
display(333,"Rossum")
display(444,"Gosling","Developer",777.88,"Java Deveops")