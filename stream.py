#stream.py
import requests
import tweepy
from secrets import *
import time


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Twitter requires all requests to use OAuth for authentication
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def retweet_status(status):
    excluded_words = ["job","monty python","RT"]
    can_retweet = 1
    for s in excluded_words:
        if  s in status.text:
            can_retweet = 0

    if can_retweet == 1:
        time.sleep(2 * 60)
        api.create_favorite(status.id)
        print("retweet!")



# create a class inheriting from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        print(status.text)
        retweet_status(status)



myBot = BotStreamer()
stream = tweepy.Stream(auth,myBot)
stream.filter(track=['wimbledon'])

