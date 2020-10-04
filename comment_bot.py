import tweepy as tp
import logging
import os
from time import sleep


import config

usersname = '@Mbuhari'

def comment_():
    time_line = api.user_timeline(usersname, count = 1)
    user = api.get_user(username)
    for tweet in time_line:
        name = tweet.user.screen_name
        id = tweet.id
        print(f"{tweet.user.name} said {tweet.text} with {id}" )
        api.update_status("#Endsarznow", in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)
        api.update_status(name "Just tweeted")
        print('done')
        sleep(5)
    
    
