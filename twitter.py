import tweepy
from collections import Counter
from tweepy import OAuthHandler
import re

consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_token = 'YOUR ACCESS TOKEN'
access_token_secret = 'YOUR ACCESS TOKEN SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

acc= raw_input("Give a screen name of a twitter user: ")

while True:  #validate user's existence
	try:
		api.get_user(acc)
		break
	except tweepy.TweepError:
		print "Wrong screen name"
		acc= raw_input("Give a screen name of a twitter user: ")

tweets = api.user_timeline(screen_name = acc,count=10,tweet_mode="extended")
out=[[tweet.full_text.encode("utf-8")] for tweet in tweets]

words=[]
for i in range (len(out)):
	str=" ".join(out[i])
	str1=str.replace("\xe2\x80\x99", "")		#remove apostrofes
	str2=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', str1)  #remove hyperlinks
	words.append(re.findall(r'\w+', str2.lower()))

final=[]
for i in range (len(words)):
	for j in words[i]:
		final.append(j)
res= Counter(final)
w= res.most_common()[0]
print "The most common word in the last 10 tweets of user:",acc,"was the word:",w[0],"and it was used:",w[1],"times"