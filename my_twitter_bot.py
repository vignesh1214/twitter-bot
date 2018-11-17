import tweepy
import time


CONSUMER_KEY='AyKsfndL6WlssUzc6jvCyvujG'
CONSUMER_SECRET='WMbNtQLZSlNp5VeQJJIu17snxboiXghS58TVF9Qb0hAyZOtgoi'
ACCESS_KEY='1061398020506316800-hDchNMw8lbZvn8nfQ5mEJ9nN6mfRVa'
ACCESS_SECRET='M9RVcx7al9fiDNJiEjlbDjgwrfJMmLM9MgDpo9IvVPJzb'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)




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


