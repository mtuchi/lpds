# Twitter Sentiment Analysis
import os
import tweepy
from textblob import TextBlob
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
public_tweets = api.search('prisonstrippers')
for tweet in public_tweets:
    print tweet.text
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
