import tweepy as tp
import logging
import os
from time import sleep

auth = tp.OAuthHandler('pIZw54XtvVuGZM4TTJYHZrFX1', '6x1ohdPHRdFnSrUGUo6qbEup3O7eiVk5mMNpnFXcWrLQPNVhTC')
auth.set_access_token('1305611268447928320-MA3D0D1Ay41wjefcRmrxKr08Ub12VM', 's0EAbYg9gKIM8qoq0XjDpCCA3mToGPvQxkntPv6AWbtVI')
api = tp.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    


def comment(usersname):
    for user in usersname:
        time_line = api.user_timeline(user, count = 1)
        users = api.get_user(user)
        for tweet in time_line:
            id = tweet.id
            print(f"{tweet.user.name} said {tweet.text} with {id}" )
            try:
                api.update_status("#EndSWAT #5for5 #SarsMustEnd", in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
                api.update_status(usersname + '    ' + "Just tweeted")
                #print(users)
                #success = True
            except:
                pass
    
    
