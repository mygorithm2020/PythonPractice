import datetime
s = datetime.datetime.now()
print(s)
q = datetime.date
print(q)

dtStr = "2016-09-15 00:00:00.000"
dt = datetime.datetime.strptime(dtStr, "%Y-%m-%d %H:%M:%S.%f")
print(dt)
dt -= datetime.timedelta(seconds= 3.5)
print(dt)