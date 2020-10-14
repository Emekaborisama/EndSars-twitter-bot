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
    


def tweet_mention():
    tweets= api.mentions_timeline(tweet_mode = 'extended')
    try:
        for tweet in tweets:
            api.update_status('##EndSWAT #5for5 #SarsMustEnd', in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)
            print('replied the mentioned')
        #success = True
    except:
        print('We pass')
        pass
    #return success
