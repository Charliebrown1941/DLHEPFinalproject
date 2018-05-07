# -*- coding: utf-8 -*-
"""
Created on Wed May 02 12:26:57 2018

@author: Brandon
"""

import tweepy, tweepy.api
from tweepy import OAuthHandler
import csv #Import csv
consumer_key = '55qjODG9hyiIFvOG71gNF7D7g'
consumer_secret = '94g3Q7CYW9kCS4RUyaEnhFlN0jITzGJ3afrz8ErvRL8BVuL3LI'
access_token = '988229022835503106-BMUMV49LE7LTiqk2BEXZ35ulne4m4a4'
access_secret = 'UUhnN8e41OgXoAtzOetudpzKzsYkVcYyGUBkKqzeIAXse'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# Open/create a file to append data to
csvFile = open('usertimeline.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.home_timeline).items(200):

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
csvFile.close()
    
#convert csv to list
with open('usertimeline.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print your_list