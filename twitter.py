import tweepy
import time
import os 
from os import environ

CONSUMER_KEY=os.environ.get('mconsumer_key')
CONSUMER_SECRET=os.environ.get('mconsumer_secret')
ACCESS_KEY=os.environ.get('maccess_key')
ACCESS_SECRET=os.environ.get('maccess_secret')

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

searchQuery = '#momo'
nrTweets = 20

for tweet in tweepy.Cursor(api.search, q = searchQuery, result_type='recent').items(nrTweets):                
    try: 
        print('Tweet Retweet')
        tweet.retweet()
        time.sleep(15)
    except tweepy.TweepError as e:
        print (e.reason)
    except StopIteration:
        break

