import tweepy as tp
import logging
import os
from time import sleep

logger = logging.getLogger()


auth = tp.OAuthHandler('HIKNUXgmi73ArgiofX7TsHWXG', 'jqCot90uTJbeaVivJQdKB7i6sOVc6nnU8gUrB6llMixOexUtAH')
auth.set_access_token('1305611268447928320-mUXqZUiDrTHxVB1gd5JowLvNjF0JkB', 'gOj1wF0IEKetKrA61UoSoWWU2BOLk6ppdknwQsmoQGK3p')
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
        
        
