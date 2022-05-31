import numpy as np
import pandas as pd
from Praw_Wrapper import subredditScrape, redditorScrape
from Tweepy_Wrapper import tweetScrape, userScrape
import automateScraping

autoScraping = True
industryDict1 = {'Lenovo': [['Lenovo','LenovoLegion','Thinkpad'], ['#Lenovo','Lenovo Computer','lenovo legion', '@Lenovo', '@LenovoSupport', 'ThinkReality', '#X1Carbon', '#Ideapad', '#LenovoF1', '#LenovoRising']]}
industryDict2 = {'Netflix': [['netflix','NetflixBestOf','bestofnetflix'], ['#netflix','@netflix']]}


brandSearches = [industryDict2]

command = None

df = pd.DataFrame(columns=['topic','stream','text', 'time of creation', 'location', 'ups', 'favorite_count'])
dfAdd = df

while command != 'exit' and autoScraping == False:
    if command == 'export':
        filename = 'scrapeDF_' + str(np.random.randint(100,999)) + '.csv'
        df = df.reset_index(drop=True)
        df.to_csv(filename)
        print('Exported filename: ' + filename)
        break
    if command =='df size':
        print('df size: ' + str(df.index.size))

    command = input('Please command scrape query number, \'df size\', \'export\', or \'exit\' \n'
                    '{Praw: subreddit (1), redditor (not working); Tweepy: twitter (3), twitter user (not implemented)}: \n'
                    '>? ')
    dfAdd = None
    match command:
        case '1':
            dfAdd = subredditScrape(count=100)
        # case '2':
        #     dfAdd = redditorScrape()
        case '3':
            dfAdd = tweetScrape(count=100)
        # case '4':
        #     dfAdd = userScrape()

    if command in ['1','2','3','4']:
        print('Concatenating dfs...')
        df = pd.concat((df,dfAdd))

if autoScraping:
    for industryDict in brandSearches:
        automateScraping.autoScrape(industryDict)

exit('Scraping complete')
