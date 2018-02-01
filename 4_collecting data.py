import tweepy
import requests
from threading import Thread
from http.client import IncompleteRead
from twython import TwythonStreamer
from twython import Twython


APP_KEY = "xUFUl2wvslXiBhWJwujcPjLGy"
APP_SECRET = "hLzpiH10cFSMqkHM7B3D7xMDzNqJe9Jge2PUl80CxUaAsi2cvP"
OAUTH_TOKEN = "828352648655020034-fLiKfYxbi2FLQYdlLfZ5G0ED1n6vSYp"
OAUTH_TOKEN_SECRET = "SgWNEVhEmzzUKzvHJ6LRQYMi67n9ekGtx2sADW6OAymr5"

# Creating the authentication object
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
# Setting your access token and secret
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 




twitter = Twython(APP_KEY, APP_SECRET)
authi = twitter.get_authentication_tokens()
url = (authi['auth_url'])
r= requests.get(url)
print(url)




 if os.path.exists("code.txt"):
        os.remove("code.txt")


 while True:
        if not os.path.exists("code.txt"):
            time.sleep(5)
            logging.debug(
                "'code.txt' file doesn't exists, waiting to start listening"
                " to twitter until it is created"
            )
        else:
            pincode = 0
            with open("code.txt") as f:
                pincode = int(f.read().strip())
                logging.info("Pincode read succesfully:" + str(pincode))
            return str(pincode)

        
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    final_step = twitter.get_authorized_tokens(pincode)
    logging.debug("Old OATH_TOKEN: " + str(OAUTH_TOKEN))
    logging.debug("Old OAUTH_TOKEN_SECRET: " + str(OAUTH_TOKEN_SECRET))
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    logging.debug("New OATH_TOKEN: " + str(OAUTH_TOKEN))
    logging.debug("New OAUTH_TOKEN_SECRET: " + str(OAUTH_TOKEN_SECRET))
   

             
