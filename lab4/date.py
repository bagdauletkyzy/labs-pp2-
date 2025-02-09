import datetime

# 1
t = datetime.date.today()
five_days_ago = t - datetime.timedelta(days=5)

print(f"\nCurrent date: {t}")
print(f"Date 5 days ago: {five_days_ago}\n")


# 2
t = datetime.date.today()
yesterday = t - datetime.timedelta(days=1)
tomorrow = t + datetime.timedelta(days=1)

print(f'\nYesterday: {yesterday}\nToday: {t}\nTomorrow: {tomorrow}\n')


# 3
current = datetime.datetime.now()
date_without_microseconds = current.replace(microsecond=0)

print(f"\nCurrent datetime with microseconds: {current}")
print(f"Datetime without microseconds: {date_without_microseconds}\n")


#4
date1 = datetime.datetime(2025, 2, 5, 14, 33, 27)
date2 = datetime.datetime.now()

time_difference = date2 - date1
seconds_difference = time_difference.total_seconds()

print(f"\nDifference between the two dates in seconds: {seconds_difference}\n")
