from tweet import Tweet
import joblib

class TweetStore:

    def __init__(self):
        self.db = joblib.load('flask_tweets.pkl')

    def tweets(self):
        tweets = []
        
        for tweet_obj in self.db:
            tweets.append(Tweet(tweet_obj)) 

        return tweets

