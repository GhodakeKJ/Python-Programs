#Prog7.py
# Program Which Displays Keyword Length Variable Arguments 

def userinfo(city,*k1,crs="Python",**kvr):
	print("="*50)
	print("Variable Length Arguments")
	print("="*50
	for val in k1:
		print("\t".format(val))
	print("="*50)
	print("KeyWord Length Variable Arguments")
	print("="*50
	print("Living City :{}".format(city))
	print("Course :{}".format(crs))
	for k,v in kvr.items():
		print("\t{}====>\t{}".format(k,v))
	print()
	print("="*50)


#Main Program
userinfo("Maharashtra",10,20,30,sno=101,sname="Karan",hobby1="Cricket",hobby2="Game")
userinfo("Hyderabad",12,5555,567834,"JK","LK",sub1="Marathi",sub2="English",sub3="Hindi")
userinfo("Banglore","Java","UI","Ruby",eno=1001,ename="Rossum",dev="XYZ")
userinfo("Mumbai",eno="1010",ename="Jack",sal=3.4,roll="Manager")

