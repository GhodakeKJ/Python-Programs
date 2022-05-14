#Prog6.py
# Program Which Displays Keyword Length Variable Arguments 

def information(crs,cnt="India",*a,**KeyValue):
	print("="*50)
	print("\tCourse :{}".format(crs))
	print("\tType Of :{}",type(a))
	print("\tCountry :{}".format(cnt))
	print("\tType Of KeyValue:{}".format(KeyValue))


#Main Program

information("Python",10,20,30,sno="101",sname="Karan",city="Maharashtra")
information("Java",10,20,30,sno="101",sname="Karan",city="Maharashtra")
