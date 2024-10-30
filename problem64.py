#learn calender
import calendar
mo,da,ye=input().split()

day_number = calendar.weekday(year=int(ye), month=int(mo), day=int(da))
day_name = calendar.day_name[day_number]
print(day_name)