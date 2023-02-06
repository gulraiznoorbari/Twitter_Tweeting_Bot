import os
import dotenv
import datetime
import twitter

# Load environment variables
dotenv.load_dotenv()

"""
    !IMPORTANT!
    TODO: Need elevated access to Twitter Developer Account to post tweets (currently there is a bug in Twitter not allowing me to enter my phone number to verify my account).
"""

# Get environment variables
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_KEY_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret)

print(auth.VerifyCredentials())

# Get the current date
date_today = datetime.datetime.now()

# Tweet Message:
tweet_text = f"Today's date is {date_today.strftime('%B %d, %Y')}..."

# Post the tweet:
tweet = auth.PostUpdate(tweet_text)

print(tweet.text)
