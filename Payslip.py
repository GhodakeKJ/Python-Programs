#5/3/2022
eno=int(input("Enter Employee Number :"))
ename=input("Enter Employee Name:")
basicsal=float(input("Enter Employee Basic Salary:"))
if(basicsal<=0):
print(" {} is invalid salary...plz enter employee +ve Salary".format(basicsal))
else:
	if(basicsal>=0):
		ha=basicsal *(15/100)
		ta=basicsal *(20/100)
		cca=basicsal *(13/100)
		hra=basicsal *(2/100)
		pgf=basicsal *(3/100)
		lic=basicsal *(2/100)
	else:
		ha=basicsal *(25/100)
		ta=basicsal *(20/100)
		cca=basicsal *(15/100)
		hra=basicsal *(2/100)
		pgf=basicsal *(1/100)
		lic=basicsal *(2/100)
netsal=(basicsal+ha+ta+cca+hra)-(pgf+lic)
print("="*50)
print("E M P L Y E E  P A Y M E N T  S L I P ")
print("="*50)