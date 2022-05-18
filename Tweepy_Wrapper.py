import os
import tweepy
import pandas as pd

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

twitter_auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
twitter_api = tweepy.API(twitter_auth)


def tweetScrape(count=50):
    '''

    https://docs.tweepy.org/en/stable/api.html#search-tweets
    :return:
    '''
    columns=['text', 'time of creation', 'location', 'ups', 'favorite_count']
    data = []

    # geocode = input('Please input geocode (example: 37.7821120598956,-122.400612831116,3km)')
    geocode = '37.7821120598956,-122.400612831116,3km'
    query = input('Please input search term (hashtag search, include \'#\'):')
    print('Scraping Twitter...')
    api_response = twitter_api.search_tweets(q=query, count=count)

    for tweet in api_response:
        dt_tweet = tweet.created_at.isoformat()
        data.append([tweet.text,dt_tweet[:-6],geocode,None,tweet.favorite_count])

    return pd.DataFrame(data,columns=columns)

def userScrape(count=50):
    '''

    :return:
    '''

    raise NotImplementedError



