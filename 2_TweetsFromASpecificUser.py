import tweepy
consumer_key = "xUFUl2wvslXiBhWJwujcPjLGy"
consumer_secret = "hLzpiH10cFSMqkHM7B3D7xMDzNqJe9Jge2PUl80CxUaAsi2cvP"
access_token = "828352648655020034-fLiKfYxbi2FLQYdlLfZ5G0ED1n6vSYp"
access_token_secret = "SgWNEVhEmzzUKzvHJ6LRQYMi67n9ekGtx2sADW6OAymr5"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 
# The Twitter user who we want to get tweets from
name = "Charul"
# Number of tweets to pull
tweetCount = 5

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print(tweet.text)
   print(tweet.created_at)
   print(tweet.user.screen_name)
   print(tweet.user.location)
   print("\n")