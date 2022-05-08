import os
import praw
import pandas as pd

limit = 5

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
user_agent = os.environ.get("user_agent")
reddit_read_only = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)

def subredditScrape():
    '''
    This function returns a pd.Dataframe as a result of scraping one or multiple subreddits
    https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html
    :param subreddits:
    :return:
    '''
    timeframe = input('Please input time filter (all,hour,day,week,month,year): ')
    hottopnewcont = input('Please specify stream type (hot, top, new, controversial): ')
    phraseSearch = input('Is this a phrase search? (y/n): ')
    phrase = None
    if phraseSearch == 'y':
        phrase = input('Please input search phrase: ')

    subreddit_name = input('Please specify a subreddit or comma separated list of subreddits (\'all\' if reddit-wide): ')
    subreddit_name = subreddit_name.split(',')
    for i in range(len(subreddit_name)):
        subreddit_name[i] = subreddit_name[i].strip()

    for srName in subreddit_name:
        subreddit = reddit_read_only.subreddit(srName)
        toKeep = input('Subreddit ' + srName + ' , found: ' + subreddit.display_name + ' Keep? (y/n):')
        if toKeep != 'y':
            continue

        if phraseSearch == 'n':
            match hottopnewcont:
                case 'hot':
                    api_return = subreddit.hot(time_filter=timeframe, limit=limit)
                case 'top':
                    api_return = subreddit.top(time_filter=timeframe, limit=limit)
                case 'new':
                    api_return = subreddit.new(time_filter=timeframe, limit=limit)
                case 'controversial':
                    api_return = subreddit.controversial(time_filter=timeframe, limit=limit)
                case _:
                    print('Invalid stream type')
                    return None
        elif phraseSearch == 'y':
            api_return = subreddit.search(phrase, time_filter=timeframe, limit=limit, sort=hottopnewcont)
        else:
            print('Invalid input')
            return None

    raise NotImplementedError



def redditorScrape():
    '''
    This function returns a pd.Dataframe as a result  of scraping one or multiple redditors
    https://praw.readthedocs.io/en/stable/code_overview/models/redditor.html
    :return:
    '''
    timeframe = input('Please input time filter (all,hour,day,week,month,year): ')
    hottopnewcont = input('Please specify stream type (hot, top, new, controversial): ')
    phraseSearch = input('Is this a phrase search? (y/n): ')
    phrase = None
    if phraseSearch == 'y':
        phrase = input('Please input search phrase: ')

    redditor_name = input('Please input redditor name(s):')
    redditor_name = redditor_name.split(',')
    for i in range(len(redditor_name)):
        redditor_name[i] = redditor_name[i].strip()

    for rdName in redditor_name:
        redditor = reddit_read_only.subreddit(rdName)
        toKeep = input('Subreddit ' + rdName + ' , found: ' + redditor.display_name + ' Keep? (y/n):')
        if toKeep != 'y':
            continue

        if phraseSearch == 'n':
            match hottopnewcont:
                case 'hot':
                    api_return = redditor.hot(time_filter=timeframe, limit=limit)
                case 'top':
                    api_return = redditor.top(time_filter=timeframe, limit=limit)
                case 'new':
                    api_return = redditor.new(time_filter=timeframe, limit=limit)
                case 'controversial':
                    api_return = redditor.controversial(time_filter=timeframe, limit=limit)
                case _:
                    print('Invalid stream type')
                    return None

        elif phraseSearch == 'y':
            api_return = redditor.search(phrase,phrasetime_filter=timeframe, limit=limit, sort=hottopnewcont)
        else:
            print('Invalid input')
            return None

    raise NotImplementedError



