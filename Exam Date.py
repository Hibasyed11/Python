import calendar
year=2025
month=11
exam=int(input("When is your exam? "))
cal=calendar.monthcalendar(year,month)
for week in cal:
    row=""
    for day in week:
        if day==exam:
            row += f"{day:2d}* "
        else:
            row+= f"{day:2d} " if day != 0 else " "
    print(row)
print(calendar.month(year,month))