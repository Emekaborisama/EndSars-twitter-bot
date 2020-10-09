import tweepy as tp
import logging
import os
from time import sleep


auth = tp.OAuthHandler('HIKNUXgmi73ArgiofX7TsHWXG', 'jqCot90uTJbeaVivJQdKB7i6sOVc6nnU8gUrB6llMixOexUtAH')
auth.set_access_token('1305611268447928320-mUXqZUiDrTHxVB1gd5JowLvNjF0JkB', 'gOj1wF0IEKetKrA61UoSoWWU2BOLk6ppdknwQsmoQGK3p')
api = tp.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    


def comment(usersname):
    for user in usersname:
        time_line = api.user_timeline(user, count = 3)
        users = api.get_user(user)
        for tweet in time_line:
            id = tweet.id
            print(f"{tweet.user.name} said {tweet.text} with {id}" )
            try:
                api.update_status("#EndSarsNow, #EndSars, #EndSarsNow!", in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
                api.update_status(usersname + '    ' + "Just tweeted")
                #print(users)
                #success = True
            except:
                pass
    
    
