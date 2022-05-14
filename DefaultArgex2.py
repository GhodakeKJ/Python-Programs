def display(sno,sname,marks,course="Python",country="India"):

    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,course,country))


    #Main Program
print("=" * 80)
print("   SNo \t\tSName \t\tMarks \t\tCourse \t\t Country")
print("-" * 80)
display(1,"Karan",78.80,"Python")
display(2, "Scott", 58.80, course="Django")
display(3, "Tiger", 77.80, "Python")
display(4, "Aniket", 58.80, "Python", country="Japan")
display(5, "Rossum", 79.80, course="DataSci")
display(6, "Jacket", 58.80, "Python", country="Tokoyo")
print("=" * 80)