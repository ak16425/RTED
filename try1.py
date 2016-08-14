import json
import pandas as pd
from collections import Counter

tweets_data_path = '/home/annie/Desktop/final/flood.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
	keys = tweet.keys()
        tweets_data.append(tweet)
	if 'coordinates' in tweet:
		print tweet['coordinates'][0]
    except:
        continue
print len(tweets_data)

#tweets_data = tweets_data.encode('ascii', 'ignore').decode('ascii')

inout_Text = []
inout_Location=[]
inout_retweet=[]
inout_place=[]

for record in tweets_data:
  	if record.get('text'):
		inout_Text.append(record.get('text'))
thefile_text=open('/home/annie/Desktop/final/tweets.txt',"w")

for item in inout_Text:
  item = item.encode('ascii', 'ignore').decode('ascii')
  thefile_text.write("%s\n" % item)


str1=''
for item in inout_Text:
  item = item.encode('ascii', 'ignore').decode('ascii')
  str1= str1+item

##############################################################################


import requests
payload={'text':str1,'entity_type' : 'places_eng','show_alternatives':'false','apikey':'532378c2-ceb9-45b7-8b2a-34d873d4b667'}
r = requests.post("https://api.havenondemand.com/1/api/sync/extractentities/v2", data=payload)
str2=r.text
#print str2
tweets_data2 = []
tweets_file2 = r.text
#print tweets_file2
for line in tweets_file2:
    try:
        tweet2 = json.loads(line)
        tweets_data2.append(tweet2)
    except:
        continue
tweets2 = pd.DataFrame()
#tweets2['tweet2'] = map(lambda tweet2: tweet2['normalized_text'] if 'normalized_text' in tweet2 else None, tweets_data2)
#tweets2['nt'] = [tweet2["entities"]['normalized_text'] if "entities" in tweet2 and tweet2["entities"]['normalized_text']
#		else np.nan for tweet2 in tweets_data2]
#print tweets2['nt']


#thefile_text2=open('/home/annie/Desktop/final/hpe.txt',"w")









arr = []
arr2 = []

json_dict = json.loads(str2)
for dom in json_dict['entities']:
	str1=''
	str1=''+(dom['normalized_text'])
	str1=str1.encode('ascii', 'ignore').decode('ascii')
	#dom['normalized_text'] = (dom['normalized_text']).encode('ascii', 'ignore').decode('ascii')
	#print 'nt : %s' %(dom['normalized_text'])
	arr.append(dom['normalized_text'])

arr2=(map(str, arr))
arr2.append('Virginia')
#print(Counter(arr2).keys())
#print(Counter(arr2).values())


#print(arr2)





#print len(tweets_data)






###############################################################################


##############################################################################
tweets = pd.DataFrame()

import numpy as np
tweets['Location'] = [tweet["user"]['location'] if "user" in tweet and tweet["user"]['location']
                      else np.nan for tweet in tweets_data]
tweets['time_zone'] = [tweet["user"]['time_zone'] if "user" in tweet and tweet["user"]['time_zone']
                       else np.nan for tweet in tweets_data]


#print(tweets['Location'].dropna())

#print(tweets['time_zone'].dropna())

str9=''
str9=str9+(tweets['Location'].value_counts().idxmax())
x=(tweets['Location'].value_counts().max())
print (str9)
print x
res= "LOC_ALERT: "+str9 +"tweeted "+ str(x)+ "times" 
print res

str10=''
str10=str10+(tweets['time_zone'].value_counts().idxmax())
y=(tweets['time_zone'].value_counts().max())
print (str10)
print y
res1=res+ " TZ_ALERT: "+str10 +"has been tweeted "+ str(y)+ "times" 
print res1


import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "764357668710395904-S07jCPrllOeo615TovAqPmWwUWr0xkm"
access_token_secret = "Yi3LEM2zxXPeMQwF2iVQEsmROJmMVBFeMOixxg4cFx5sk"
consumer_key = "AGqeL2Lfgr6C8dmho6hraRNGs"
consumer_secret = "q91CdDWFzaZnN8uGtQmCOGBL600HNFJzo72tMRTqBcrJuYSqJq"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(res1)
#print tweets_by_loc['Location']

#tweets_by_tz=tweets['time_zone'].value_counts()

#print arr5

#print tweets_by_tz

