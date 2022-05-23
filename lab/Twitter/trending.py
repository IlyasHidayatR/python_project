#crawling the trending topics from twitter
import tweepy
import csv
import pandas as pd


# Twitter API credentials
api_key = 'KWW812xqlKvqM1yhXaOWz4oph'
api_key_secret = 'Pa22U02YD0gB8Tyo6ypIzLidjStx3uCvLylGJ0d4hGWXeXbV9N'
access_token = '763531359444881408-pYPOpdpDJHnsrXxkMfhi4N2LIuWdkQf'
access_token_secret = 'r7vt0YFJZJJeQ0XSeASVKdyrSKNnRnR00hWpMLxOWEVmT'
tweetsPerQry = 100
maxTweets = 100
maxId = -1
tweetCount = 0


# Twitter OAuth
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Crawler function to get trending topics
def get_trending_topics(woeid):
    trends = api.get_place_trends(woeid)
    for trend in trends[0]["trends"]:
        print(trend["name"])
        print(trend["url"])
        print(trend["tweet_volume"])
        print("\n")


# Get trending topics for indonesia
get_trending_topics(23424848)