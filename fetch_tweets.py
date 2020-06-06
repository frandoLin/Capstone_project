#!/usr/bin/env python
# coding: utf-8
import tweepy
import json


#Use Twitter API to fetch the tweets containing the hashtag #reopen

with open('api.json', 'r') as json_file:
    twitter_api = json.load(json_file)

consumer_key = twitter_api['consumer_key']
consumer_secret = twitter_api['consumer_secret']
access_token = twitter_api['access_token']
access_token_secret = twitter_api['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit= True)

class SearchTweets:
    
    def __init__(self, hashtags):
        
        if type(hashtags) == str:
            self.hashtags = f'#{hashtags}'
        elif type(hashtags) == list:
            self.hashtags = " OR ".join([f'#{x}' for x in hashtags])
        else:
            print('input error, the type of hashtags should be string or a list of string')            
    
    def fetch_tweets(self):
        
        file = open(f"twitter_{self.hashtags}.txt", "w")
        
        #While Filter API can fetch streaming data, Search API is a more efficient way for my project 
        # Search the matched tweets within the recent 7 days
        cursor = tweepy.Cursor(api.search, q = self.hashtags, count= 100, result_type = 'recent', lang = 'en',
                                tweet_mode = 'extended').items()

        for status in cursor:

            #status is json which is an object so hasattr() works but the method not work for dictionary

            if not hasattr(status, "retweeted_status"):  # Check if Retweet

                tweet = status._json
                file.write(json.dumps(tweet) + '\n')

        file.close() 





