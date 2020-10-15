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
    


def like_rt():
    for tweet in tp.Cursor(api.search, q = '#EndSars').items(1):
        print('Tweet by: @' + tweet.user.screen_name)
    try: 
        tweet.retweet()
        tweet.favorite()
        print('retweeted')
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed the user')
            ##success = True
    except tp.TweepError as e:
        print(e.reason)
    #return success
        
        
