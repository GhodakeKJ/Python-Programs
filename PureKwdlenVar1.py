def fun1(sno,sname,*details,cnt="India",crs="English",**Marks):
    print("=" * 60)
    print("Student Number   :{}".format(sno))
    print("Student Name     :{}".format(sname))
    print("================================================")
    print("Details Of Student :")
    for val in details:
        print("\t{}".format(val))
    print("="*60)
    print("Country Of Student :{}".format(cnt))
    print("Course Of Student  :{}".format(crs))
    print("=" * 60)
    for k,v in Marks.items():
        print("\t{} ====> \t{}".format(k,v))
    print("=" * 60)

#Main Program
fun1(101,"Rossum","Python","Django","Machine Learning",Marathi=91,Hindi=97,Maths=85,Science=89)
fun1(102,"Ritche","Cricket","Read","Gaming",Marathi=91,Hindi=97,Maths=85,Science=89)
fun1(103,"Karan","Programming","Developing Games","Creating Websites",Marathi=91,Hindi=97,Maths=85,Science=89)