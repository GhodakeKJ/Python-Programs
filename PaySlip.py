#Payslip.py
eno=int(input("ENTER THE EMPLOYEE NUMBER :"))
ename=input("ENTER THE EMPLOYEE NAME :")
basicsal=float(input("ENTER THE EMPLOYEE BASIC SALARY :"))
if(basicsal<=10000):
    print("\tInvalid Salary Plz Enter +ve Salary :")
else:
    if(basicsal>=10000):
        ta=basicsal*(10/100)
        da=basicsal*(20/100)
        hra=basicsal*(15/2)
        cca=basicsal*(2/100)
        gpf=basicsal*(2/100)
        lic=basicsal*(2/100)
    else:
        ta = basicsal *(15 / 100)
        da = basicsal *(25 / 100)
        hra = basicsal *(20 / 2)
        cca = basicsal *(3 / 100)
        gpf = basicsal *(1 / 100)
        lic = basicsal *(1 / 100)
#calculate the netsal
netsal=(basicsal+ta+da+hra+cca)-(gpf+lic)
#Displays Employee Slip
print("*"*50)
print("E M P L O Y E E    P A Y    S L I P ")
print("*"*50)
print("\tEMPLOYEE NUMBER {}".format(eno))
print("\tEMPLOYEE NAME {}".format(ename))
print("\tEMPLOYEE BASIC SALARY {}".format(basicsal))
print("\tEMPLOYEE TA {}".format(ta))
print("\tEMPLOYEE DA {}".format(da))
print("\tEMPLOYEE HRA {}".format(hra))
print("\tEMPLOYEE CCA {}".format(cca))
print("\tEMPLOYEE GPF {}".format(gpf))
print("\tEMPLOYEE LIC {}".format(lic))
print("*"*50)
print("EMPLOYEE NET SALARY={}".format(netsal))
print("*"*50)