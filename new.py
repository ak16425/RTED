from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
#%matplotlib inline
#import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.style.use('ggplot')

#Variables that contains the user credentials to access Twitter API 
access_token = '764357668710395904-S07jCPrllOeo615TovAqPmWwUWr0xkm'
access_token_secret = 'Yi3LEM2zxXPeMQwF2iVQEsmROJmMVBFeMOixxg4cFx5sk'
consumer_key = 'AGqeL2Lfgr6C8dmho6hraRNGs'
consumer_secret = 'q91CdDWFzaZnN8uGtQmCOGBL600HNFJzo72tMRTqBcrJuYSqJq'

tweets_data_path = '/home/annie/Downloads/opfinal_all.txt'

tweets_data = []
tweets_coordinates = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
	#tweet1=json.loads(data)
	#tweets_coordinates=data.append(tweet1)
    except:
        continue

print len(tweets_data)

#tweet1=json.loads(data)
#latitude,longitude=tweet1["coordinates"]["coordinates"]

tweets = pd.DataFrame()

#tweets1 = pd.DataFrame()
tweets['coordinates']['coordinates'] = map(lambda tweet:tweet['coordinates'][0]['coordinates'][1] if 'coordinates' in tweet else None, tweets_data)

tweets['tweet'] = map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data)
tweets['created_at'] = map(lambda tweet: tweet['created_at'] if 'created_at' in tweet else None, tweets_data)
tweets['user_id'] = map(lambda tweet: tweet['user']['id'] if 'user' in tweet else None, tweets_data)
tweets['id_str'] = map(lambda tweet: tweet['user']['id_str'] if 'user' in tweet else None, tweets_data)
tweets['username'] = map(lambda tweet: tweet['user']['name'] if 'user' in tweet else None, tweets_data)
tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'] if 'user' in tweet else None, tweets_data)
tweets['location'] = map(lambda tweet: tweet['user']['location'] if 'user' in tweet else None, tweets_data)
tweets['followers_count'] = map(lambda tweet: tweet['user']['followers_count'] if 'user' in tweet else None, tweets_data)
tweets['friends_count'] = map(lambda tweet: tweet['user']['friends_count'] if 'user' in tweet else None, tweets_data)
tweets['created_at'] = map(lambda tweet: tweet['user']['created_at'] if 'user' in tweet else None, tweets_data)
tweets['user_lang'] = map(lambda tweet: tweet['user']['lang'] if 'user' in tweet else None, tweets_data)
tweets['following'] = map(lambda tweet: tweet['user']['following'] if 'user' in tweet else None, tweets_data)
#tweets['geo'] = map(lambda tweet: tweet['geo'], tweets_data)
#
#tweets['coordinates'] = map(lambda tweet: tweet['coordinates'], tweets_data)
#tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], tweets_data)
#tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], tweets_data)
#tweets['country'] = map(lambda tweet: tweet['place']['country'] if 'country' in tweet else None, tweets_data)
#tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
#tweets['country'] = map(lambda tweet: tweet.get('place', {}).get('country'), tweets_data)
#print (tweets1)
tweets['normalized_text'] = map(lambda tweet: tweet['normalized_text'] if 'normalized_text' in tweet else None, tweets_data)
print (tweets)



