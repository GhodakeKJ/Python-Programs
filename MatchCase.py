#Program Which implementing Arithmatic Operations by using Menu Driven Approch
#MatchCase.py
print("="*70)
print("\tA  R  I  T  H  M  A  T  I  C    O  P  E  R  A  T  I  O  N  S")
print("="*70)
print("\t1.ADDITION")
print("\t2.SUBTRACTION")
print("\t3.MULTIPLICATION")
print("\t4.DIVISION")
print("\t5.MODULO DIVISION")
print("\t6.EXPONENTIATION")
print("\t7.EXIT")
print("="*70)
ch=int(input("ENTER YOUR CHOICE :"))
match(ch):
    case 1:
        a=float(input("Enter First Value For Adddition :"))
        b= float(input("Enter Second Value For Adddition :"))
        print("Sum ({} And {})={}".format(a,b,a+b))
    case 2:
        a = float(input("Enter First Value For Subtraction :"))
        b = float(input("Enter Second Value For Subtraction :"))
        print("Sum ({} And {})={}".format(a, b, a - b))
    case 3:
        a = float(input("Enter First Value For Multiplication :"))
        b = float(input("Enter Second Value For Multiplication :"))
        print("Sum ({} And {})={}".format(a, b, a * b))
    case 4:
        a = float(input("Enter First Value For Division :"))
        b = float(input("Enter Second Value For Division :"))
        print("Sum ({} And {})={}".format(a, b, a / b))
    case 5:
        a = float(input("Enter First Value For Floor Division :"))
        b = float(input("Enter Second Value For Floor Division :"))
        print("Sum ({} And {})={}".format(a, b, a // b))
    case 6:
        a = float(input("Enter First Value Modulo For Division :"))
        b = float(input("Enter Second Value Modulo For Division :"))
        print("Sum ({} And {})={}".format(a, b, a % b))
    case 7:
        a = float(input("Enter Base :"))
        b = float(input("Enter Power :"))
        print("Sum ({} And {})={}".format(a, b, a ** b))
    case 8:exit()
    case _:print("Your Choice Of Operation Is Invalid Plz Try Again...!")
print("X" * 70)