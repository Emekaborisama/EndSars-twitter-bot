import tweepy as tp
import logging
import os
from time import sleep

logger = logging.getLogger()


auth = tp.OAuthHandler('3rFqD3xxtIPoUvdEd0PNA2fly', 's2FNdygjZRCrlECZBlmk3q3KjSgJMTjvUi1dD4SXcCdt4FA6Iw')
auth.set_access_token('1305611268447928320-ioLLdFnDhCUyvHqSyw0nT5G6XXPvb4', 'q7ZYOyJgYiSth5ZY8IohGkWSSOgGJ9R9blj2dx3HAh0DZ')
api = tp.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    


def tweet_mention():
    tweets= api.mentions_timeline(tweet_mode = 'extended')
    try:
        for tweet in tweets:
            api.update_status('#EndSarsNow', in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)
            print('replied the mentioned')
        #success = True
    except:
        print('We pass')
        pass
    #return success
