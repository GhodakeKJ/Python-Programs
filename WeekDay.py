#WeekDay.py
wd=input("ENTER WEEK DAY NAME :")
match(wd.upper()):case "MONDAY" | "TUESDAY" | "WEDNESDAY" | "THIRSDAY" | "FRIDAY" :print("{} Is A Working Day".format(wd))
case"SATURDAY" :print("{} Is A Week End Day :".format(wd))
case"SUNDAY" :print("{} Is A  Holyday :".format(wd))
case _:print("{} Is Not A Week Day".format(wd))