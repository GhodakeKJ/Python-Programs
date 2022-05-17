while(True):
    sno = int(input("Enter Student Exam Number :"))
    if(sno>=1)and(sno<=500):
        break
    print("Enter Exam Number Between 1 to 500 Only")
sname=input("Enter Student Name :")
cname=input("Enter Collage Namne :")
#Validation Of Marathi Marks
while(True):
    marathi=int(input("Enter Marks Obtained In Marathi :"))
    if(marathi>0)and(marathi<100):
        break
    print("Plz Enter Marks Between 0 To 100 Only")

# Validation Of Hindi Marks
while (True):
    hindi =int(input("Enter Marks Obtained In Hindi :"))
    if(hindi>0)and(hindi<100):
        break
    print("Plz Enter Marks Between 0 To 100 Only")

# Validation Of English Marks
while (True):
    english=int(input("Enter Marks Obtained In English :"))
    if(english>0)and(english<100):
        break
    print("Plz Enter Marks Between 0 To 100 Only")
totalmarks=marathi+hindi+english
average = totalmarks/300*100
if(marathi<40)or(hindi<40)or(english<40):
    grade="Fail"
else:
    if(totalmarks>=250)and(totalmarks<=300):
        grade="First"
    elif(totalmarks>=200)and(totalmarks<=249):
        grade="Second"
    else:
        grade="Third"
print("="*80)
print(" * S T U D E N  T  M A R K S  R E P O R T  C A R D  *")
print("="*80)
print("\tStudent Exam Number        :{}".format(sno))
print("\tStudent Full Name          :{}".format(sname))
print("\tStudent Collage Name       :{}".format(cname))
print("-"*80)
print("\t Marks Obtained In Marathi :{}".format(marathi))
print("\t Marks Obtained In Hindi   :{}".format(hindi))
print("\t Marks Obtained In English :{}".format(english))
print("-"*80)
print("\t\t Total Marks             :{}".format(totalmarks))
print("="*80)
print("\t\t Percentage              :{}".format(average))
print("\t\t You Are Grade           :{}".format(grade))
print("="*80)