import tweepy as tp
import logging
import os
from time import sleep

logger = logging.getLogger()

auth = tp.OAuthHandler('pIZw54XtvVuGZM4TTJYHZrFX1', '6x1ohdPHRdFnSrUGUo6qbEup3O7eiVk5mMNpnFXcWrLQPNVhTC')
auth.set_access_token('1305611268447928320-MA3D0D1Ay41wjefcRmrxKr08Ub12VM', 's0EAbYg9gKIM8qoq0XjDpCCA3mToGPvQxkntPv6AWbtVI')
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
            api.update_status('#EndSWAT #5for5 #SarsMustEnd', in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)
            print('replied the mentioned')
        #success = True
    except:
        print('We pass')
        pass
    #return success
