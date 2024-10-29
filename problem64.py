#learn calender
import calendar
n=int(input())
print(calendar.TextCalendar(firstweekday=6).formatyear(n))