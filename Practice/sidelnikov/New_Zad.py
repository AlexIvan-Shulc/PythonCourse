import datetime

def workday(date1, date2):
    if date1 > date2:
        sum = 1
        res = (date1 + datetime.timedelta(x) for x in range((date1 - date2).days + 1))
        for day in res:
            if day.weekday() < 5:
                sum += 1
        return sum
    elif date1 == date2:
        return 0
    else:
        print("Введено неверное значение")
date_start = datetime.date(2020, 4, 2)
date_stop = datetime.date(2020, 4, 11)
print(workday(date_stop, date_start))