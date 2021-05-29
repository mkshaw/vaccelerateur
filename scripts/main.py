"""

main.py

Scrape data from Twitter account vaccelerateur06 (Montreal) by accessing Twitter API via Tweepy. Return a list of times of day, probably formatted as datetime.

"""

import tweepy
import pandas as pd
import argparse
import os.path as osp # for getting and saving files
import json # for extracting API keys
import datetime # for extracting time information
import collections # for frequency list

# Define constants and reference points
working_dir = osp.dirname(__file__)
NUMBER_OF_TWEETS = 1500

def main():
    
    # retrieve keys from keys.txt
    with open(osp.join("keys.json")) as f:
        keys = json.load(f)
    consumer_key = keys['api_key']
    consumer_secret = keys['api_secret']

    # define auth information
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    # Create cursor to navigate the feed
    cursor = tweepy.Cursor(api.user_timeline, id="vaccelerateur06", tweet_mode="extended").items(NUMBER_OF_TWEETS) # currently hard-coded number to return; I believe 1500 is the maximum request allowed

    # save the datetime created_at contents to a list

    tweet_times = [tweet.created_at for tweet in cursor] # list comprehension version of for tweet in cursor: tweet_times.append(tweet.created_at)

    # create list of just the hours
    hours = []
    hours = list(map(lambda x: x.hour, tweet_times))
    
    # get frequency of hours
    counter = collections.Counter(hours)

    # Save hours as data
    df = pd.DataFrame.from_dict(counter, orient = 'index').reset_index() # convert counter dictionary to df
    df = df.rename(columns = {"index": "hour_gmt", 0: "number_of_tweets"}) # rename columns from defaults
    df = df.sort_values(by = "hour_gmt") # sort to be in order by hour
    
    df.to_csv(osp.join(working_dir, "..", "data", "vacc06.dat"), index = False, header = False)
    

if __name__ == '__main__':
    main()
