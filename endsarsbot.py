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


import comment_bot as c
import like_retweet as lrt
import mention as m

def main():
    usersname = ['@NigeriaGov', '@NGRPresident',
                 '@NigEducation', '@fmaviationng', '@fccpcnigeria', '@NCDCgov', '@Nigeria', '@PowerMinNigeria', '@NigeriaMFA', '@NgComCommission', '@FinMinNigeria', '@firsNigeria', '@followlasg', '@FMoCDENigeria', '@LSMOH', '@OfficialAPCNg', '@followlastma', '@PwC_Nigeria', '@NGRSenate', '@SPNigeria', '@nassnigeria', '@FRSCNigeria', '@PoliceNG', '@inecnigeria', '@MBuhari', '@drobafemihamzat', '@ProfOsinbajo', '@toluogunlesi', '@jidesanwoolu', '@Laurestar', '@tundefashola',  '@femigbaja']
    c.comment(usersname = usersname)
    lrt.like_rt()
    m.tweet_mention()
    success = True
    return success
    
    
    
while True:
    main()
    sleep(10)
