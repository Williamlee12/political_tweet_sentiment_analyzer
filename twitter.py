import tweepy
import os

auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])

api = tweepy.API(auth)

pol_tweets = api.user_timeline(screen_name='realDonaldTrump', count = 50, tweet_mode='extended')

for item in pol_tweets:
    print(item.full_text)
