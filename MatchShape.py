# Program Implementation Area Of Difference Figure By Using Menu Driven Approch
#MatchShape.py
print("*"*70)
print("\tA  r  e  a    O  f    F  i  g  u  r  e  s")
print("*"*70)
print("\tC.Circle")
print("\tT.Triangle")
print("\tR.Rectangle")
print("\tS.Square")
print("\tE.Exit")
print("*"*70)
ch=input("ENTER YOUR CHOICE :")
match(ch):case "C" | "c":
r=float(input("Enter Radius :"))
ac=3.14*r**2
print("Area Of Circle={}".format(ac))
case "S" | "s":s=float(input("Enter Side :"))
sa=s**2
print("Area Of Square={}".format(sa))
case "R" | "r":l=float(input("Enter Lenght :"))
b=float(input("Enter Breadth :"))
ar=l*b
print("Area Of Rectanle ={}".format(ar))
case "T" | "t":
a=float(input("Enter Value Of Side1 :"))
b=float(input("Enter Value Of Side2 :"))
c=float(input("Enter Value Of Side3 :"))
s=(a+b+c)/2
at=(s*(s-a)*(s-b)*(s-c)) **0.5
print("Area Of Triangle ={}".format(at))
case "E" | "e":exit()
case _:print("Your Choice Of Operation Is Invalid Try Again...!")