#Prog9.py

def display(*k):
	print("="*50)
	print("Type Of k :",type(k))
	print("Length of k:",len(k))
	print("-"*50)
	print("\t\t{}".format(k),end="    ")
	print("="*50)

#Main Program
display(10,"Karan Ghodake")
display(20,"Rossum",True,34.566)
display(30,40,5060,700,403,60,"Jack",10,20,55)