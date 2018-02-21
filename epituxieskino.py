import urllib2
import json
import datetime

d=[]
countap=[]
cur_date=datetime.datetime.now()
a=[]
while len(a)!=10:
	s= raw_input("Give your ten numbers separated by commas:\n")
	a = [int(i) for i in s.split(",")]
c=0
while c<20:		#Elegxoi twn arithmwn
	num=[]
	for i in a:
		if i<1 or i>80:
			s= raw_input("Numbers must be from 1 to 80:\n")
			a = [int(i) for i in s.split(",")]	
		else: 
			c+=1
		if i in num:
			s= raw_input("Numbers must be different between them:\n")
			a = [int(i) for i in s.split(",")]
		else: 
			c+=1
		num.append(i)
mynums= a 
print "Your numbers: ",mynums
def sigkrisi(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
    	su=0
        temp=k["results"]
        r.append(sigkrisi(mynums,temp))
        for i in r:  #Athroisma epituxiwn
        	if i>4:
        		su+=1
    countap.append(su)
    d.append(date_str)
m=0
hm=[]
for i in range(31):		#Euresh megistou arithmou epituxiwn
	if countap[i]>m:
		ind=i
		m=countap[i]
		hmera=d[i]
hm.append(hmera)
for i in range(31):
	if i!=ind and countap[i]==m:
		if d[i] not in hm:
			hm.append(d[i])
print "More (",m,") chances to win at", ", ".join(hm)

