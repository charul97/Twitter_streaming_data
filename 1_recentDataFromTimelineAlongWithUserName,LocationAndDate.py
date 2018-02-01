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

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)
   #to find the date the the tweet was created
   print(tweet.created_at)
   # to get the name of the tweeter
   print(tweet.user.screen_name)
   # to print the location of the tweeter
   print(tweet.user.location)
   print("\n")


   
