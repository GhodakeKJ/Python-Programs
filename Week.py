d=input("ENTER THE WEEK DAY :")
match(d.upper()):
case "Monday":print("{} Is A Working Day".format(d))
case "Tuesday":print("{} Is A Working Day".format(d))
case "Wednesday":print("{} Is A Working Day".format(d))
case "thursday":print("{} Is A Working Day".format(d))
case "Friday":print("{} Is A Working Day".format(d))
case "Saturday":print("{} Is A Week End Day".format(d))
case "Sunday":print("{} Is A Holiday Day".format(d))
case _:print("{} Is Not A Week Day Plz Enter Day Name...!".format(d))