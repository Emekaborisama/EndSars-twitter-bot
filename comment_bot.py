import tweepy as tp
import logging
import os
from time import sleep


import config

usersname = '@emeka_boris'

def comment__():
    time_line = api.user_timeline(usersname, count = 1)
    user = api.get_user(usersname)
    for tweet in time_line:
        name = tweet.user.screen_name
        id = tweet.id
        print(f"{tweet.user.name} said {tweet.text} with {id}" )
        try:
            api.update_status("#Endsarznow", in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
            api.update_status(usersname + '    ' + "Just tweeted")
            sleep(5)
        except:
            pass
    
    
