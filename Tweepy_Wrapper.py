import os
import tweepy
import pandas as pd



limit = 5

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

twitter_auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
twitter_api = tweepy.API(twitter_auth)


def tweetScrape():
    '''

    https://docs.tweepy.org/en/stable/api.html#search-tweets
    :return:
    '''

    geocode = '37.7821120598956,-122.400612831116,3km'
    query = input('Please input search term (hashtag search, include \'#\'):')
    api_response = twitter_api.search_tweets(q=query,count=limit)

    raise NotImplementedError


def userScrape():
    '''

    :return:
    '''

    raise NotImplementedError



