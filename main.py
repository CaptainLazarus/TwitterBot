import tweepy
import os
from dotenv import load_dotenv

MYID = 1471035724040335361

# Loading from env
load_dotenv()
API_KEY = os.getenv('CONSUMER_KEY')
API_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_KEY')
TOKEN_SECRET = os.getenv('ACCESS_SECRET')

# API auth
twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
twitter_api = tweepy.API(twitter_oauth)

# Streaming Class
class MyStreamListener(tweepy.Stream):

  def __init__(self , API_KEY , API_SECRET , ACCESS_TOKEN , TOKEN_SECRET ,api):
    super().__init__(API_KEY , API_SECRET , ACCESS_TOKEN , TOKEN_SECRET)
    self.api = api

  # the function containing the logic on what to do for each tweet
  def on_status(self, tweet):
    user_id = tweet.user.id
    tweet_id = tweet.id
    
    if tweet.in_reply_to_status_id is not None or user_id == MYID:
      pass
    else:
      if tweet.retweeted is False:
        try:
          self.api.retweet(tweet_id)
          print("Tweet retweeted successfully")
        except Exception as e:
          print(e)
      if not tweet.favorited:
        try:
          self.api.create_favorite(tweet_id)
          print("Tweet favorited successfully")
        except Exception as e:
          print(e)

#Main Program
try:
  print("Successfully logged in")
except tweepy.TweepError as e:
  print(e)
except Exception as e:
  print(e)

tweet_stream = MyStreamListener(API_KEY , API_SECRET , ACCESS_TOKEN , TOKEN_SECRET , twitter_api)
print("Works Fine till here")
tweet_stream.filter(follow=[2931820230] , track=["#100daysofcode"] , languages=['en'])