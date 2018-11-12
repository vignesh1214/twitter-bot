import tweepy
import time
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    try:
        last_seen_id = int(f_read.read().strip())
    except ValueError:
        pass
    f_read.close()


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


FILE_NAME = 'last_seen_id.txt'

stuff = api.user_timeline('558797310')

def reply_to_utd_tweet():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    stuff = api.user_timeline('558797310')
    store_last_seen_id(last_seen_id, FILE_NAME)
    api.update_status('@'+ stuff[0].user.screen_name+ ' Glory Glory Man United', stuff[0].id)



while True:
    reply_to_utd_tweet()
    time.sleep(1800)


