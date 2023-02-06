import os
import dotenv
import tweepy

# Load environment variables
dotenv.load_dotenv()

# Get environment variables
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_KEY_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


# Consumer keys and access tokens, used for OAuth
auth = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token_key,
    access_token_secret=access_token_secret)


# Post a tweet
tweet = auth.create_tweet(text="Hello, world!")
print(tweet)
