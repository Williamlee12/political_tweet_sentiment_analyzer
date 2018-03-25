import tweepy
import os

auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])
api = tweepy.API(auth)

class Get_list_of_user_tweets(object):

    def get_list(self, handle):
        pol_tweets = api.user_timeline(screen_name=handle, count = 50, tweet_mode='extended')
        tweets = [item.full_text for item in pol_tweets]
        return tweets
