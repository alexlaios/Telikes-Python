import string

def rot13(x):
	a=[]
	for i in x:
		if i in string.ascii_uppercase:
			if ord(i)>=ord("N"):
				a.append(chr(ord(i)-13))
			else:
				a.append(chr(ord(i)+13))
		elif i in string.ascii_lowercase:
			if ord(i)>=ord("n"):
				a.append(chr(ord(i)-13))
			else:
				a.append(chr(ord(i)+13))
		else: a.append(i)
	print "".join(a)
	return 
s= raw_input("Give me a string to turn into rot13: ")
rot13(s)