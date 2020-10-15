import tweepy as tp
import logging
import os

logger = logging.getLogger()

def create_api():
    auth = tp.OAuthHandler('pIZw54XtvVuGZM4TTJYHZrFX1', '6x1ohdPHRdFnSrUGUo6qbEup3O7eiVk5mMNpnFXcWrLQPNVhTC')
    auth.set_access_token('1305611268447928320-MA3D0D1Ay41wjefcRmrxKr08Ub12VM', 's0EAbYg9gKIM8qoq0XjDpCCA3mToGPvQxkntPv6AWbtVI')
    api = tp.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    
