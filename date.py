import datetime

wd= int(datetime.date.today().isoweekday())
dt= int(datetime.date.today().isoformat().split("-")[2])
year= int(datetime.date.today().isoformat().split("-")[0])
c= 0
for i in range (1,11):
	for j in range (1, 13):
		if int(datetime.date(year+i, j, dt).isoweekday())== wd:
			c+=1
print "In the next 10 years it will be ",c," times with the same weekday and monthday as today"
