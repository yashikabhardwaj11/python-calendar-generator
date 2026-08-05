import calendar
year=int(input("Enter year: "))
month=int(input("Enter month: "))
if year<0:
    print("Year cannot be negative")
elif month<1 or month>12:
    print("Month must be between 1 and 12")
else:
    print(calendar.month(year,month))
