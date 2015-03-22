#!/usr/bin/python
import sys
import time
import os
#import collections
from twitter import *

#print "IoT ready!"
print "Press CTRL + C to exit"

def read_token_file(filename):
  # Read a token file and return the oauth token and oauth token secret.
  f = open(filename)
  return f.readline().strip(), f.readline().strip()

twitter_user_creds = os.path.expanduser("~/.twitter_oauth")
twitter_consumer_creds = os.path.expanduser("~/.twitter_consumer")


#Initialize Twitter
oauth_token, oauth_secret = read_token_file(twitter_user_creds)
consumer_key, consumer_secret = read_token_file(twitter_consumer_creds)
twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, consumer_key, consumer_secret))

try:
	twitter.statuses.update(status='ITS ALIVE')
except:
	print "Something went wrong while sending the tweet: ", sys.exc_info()[1]
else:
	print "Tweet sent"

