#Prog1.py
# Program Which Displays Variable Length Arguments

def show(sno,sname,*details,crs="Python",cnt="India"):  #Function Defination-1
	print("="*50)
	print("\tStudent NUmber ={}".format(sno))
	print("\tStudent Name={}".format(sname))
	print("\tStudent Course ={}".format(crs))
	print("\tStudent Country ={}".format(cnt))
	print("Details Of Student :".format(sname))
	for val in details:
		print("\t\t",val)
	print("="*50)



#Main Program
show(101,"Rossum",76.80,"Developer",cnt="USA") #Function Call-1
show(102,"Scott",67.90) #Function Call-2
show(103,"Ritche",34.56,True,78.80,"Enggineer",cnt="UK")    #Function Call-3
show(104,"Karan",98.40,"Maharashtra","Web Developer",True,16.8)#Function Call-4
show(sno=105,cnt="Ukrean",crs="UI",sname="KKKK")