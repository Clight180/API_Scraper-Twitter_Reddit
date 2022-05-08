import numpy as np
import pandas as pd
from Praw_Wrapper import subredditScrape, redditorScrape


command = None

df = pd.DataFrame

while command != 'exit':
    command = input('Please select scrape query (Praw: subreddit (1), redditor (2); Tweepy: ')
    match command:
        case '1':
            pdOut = subredditScrape()
        case '2':
            pdOut = redditorScrape()
        case '3':
            pass


