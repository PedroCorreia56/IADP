#%%
import calendar
year=int(input("Year:"))

month=int(input("Month:"))

day=int(input("Day:"))

weekday=calendar.weekday(year,month,day)

for i in range(7):
    if i==weekday:
        print(calendar.day_name[i])
# %%
import time
date=input("Date:")

st=time.strptime(date,'%Y-%m-%d %H:%M:%S')
month=""
if st.tm_mon<10:
    print("{}/0{}/{} {}h {}min {}s".format(st.tm_mday,st.tm_mon,st.tm_year,st.tm_hour,st.tm_min,st.tm_sec))
else:
    print("{}/{}/{} {}h {}min {}s".format(st.tm_mday,st.tm_mon,st.tm_year,st.tm_hour,st.tm_min,st.tm_sec))

ta mal
# %%
import datetime
date1=input("Date1:")
date2=input("Date2:")
dat_foro="%d/%m/%Y"

dt1=datetime.datetime.strptime(date1,dat_foro)


dt2=datetime.datetime.strptime(date2,dat_foro)

dif=dt2-dt1

print("Number of days between dates={}".format(dif.days))

# %%
import dateutil
import datetime as dt

n=int(input("Number of dates:"))
date=[]
place=[]
for i in range(n):
    line=input()
    date.append(line.split(", ")[0])
    place.append(line.split(", ")[-1])


dates=[]
for i in range(n):
    parte=dateutil.parser.parse(date[0])
    dates.append(dt.datetime(parte.year,parte.month,parte.day,parte.hour,parte.minute,parte.second,tzinfo=dateutil.tz.gettz(place[i])))

dates.sort()

for i in range(n):
    print("{}, {}".format(dates[i],dates[i].tzname()))

# %%
