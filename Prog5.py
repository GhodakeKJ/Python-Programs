##Prog5.py
# Program Which Displays Variable Length Arguments by Using Find The Sum Of Numbers

def showinfo(city,**kvr):
	print("="*50)
	print("Type Of Object :",type(kvr))
	print("\t City :".format(city))
	for x,y in kvr.items():
		print("\t\t{}====>{}".format(x,y))

#Main Program
showinfo("Maharashtra",sno=101,sname="Karan",crs="Python",sno1=101)
showinfo("Hyderabad",s1="Java",s2="Python",s3="Django")