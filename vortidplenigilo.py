#!/usr/bin/env ipython
# This is intended to be run on a cronjob

import tweepy
from creds import consumer_key, consumer_secret, access_token, access_token_secret
from soup import tweet_soup
from parse_EO_full import eo_to_en
import random

# --- set up API --- #
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# --- generate a tweet --- #
# ... try to succeed ... #
success = False
while not success:
    root = random.choice(list(eo_to_en.keys()))
    root_meaning = eo_to_en[root]
    try:
        assert root.count(' ') == 0
        tweet = tweet_soup(root, root_meaning)
        assert len(tweet) < 140
        success = True
        print(tweet)
    except AssertionError:
        pass

# --- tweet yo --- #
api.update_status(status=tweet)
