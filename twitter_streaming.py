#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#User details to access Twitter API 
access_token = "764357668710395904-S07jCPrllOeo615TovAqPmWwUWr0xkm"
access_token_secret = "Yi3LEM2zxXPeMQwF2iVQEsmROJmMVBFeMOixxg4cFx5sk"
consumer_key = "AGqeL2Lfgr6C8dmho6hraRNGs"
consumer_secret = "q91CdDWFzaZnN8uGtQmCOGBL600HNFJzo72tMRTqBcrJuYSqJq"


#To print received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['flood','floods'])	#keywords to be looked for in real-time tweets
