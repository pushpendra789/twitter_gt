#!/usr/bin/python2

import tweepy
import sys 
topic=sys.argv[1]
consumer_key=''
consumer_sec=''
#by using above keys we use authentication handler
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#here auth is token by consumer key and secret
access_key=''
secret_key=''
#connection to data srever with access and secret key by using above token
print(dir(auth))
auth.set_access_token(access_key,secret_key)
#connecting to twitter api with token that is stored in auth
connected=tweepy.API(auth)

#searching topics
tweet=connected.search(topic)

#converting into text

for i in tweet:
	
	print i.text
