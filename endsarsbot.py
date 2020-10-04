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
    


import comment as c
import like_retweet as lrt
import mention sd m

if __name__ == '__main__':
    c.comment_()
    lrt.like_rt()
    m.tweet_mention()