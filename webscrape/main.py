import datetime
from datetime import datetime

import pandas as pd

from src.twitter_scrape import ClassTwitterScrape
Scrape = ClassTwitterScrape()

tweets_df = Scrape.fetch_dataframe()

tweets_df['date'] = pd.to_datetime(tweets_df['date'])
# create a session for every 5 min
# tweets_df['session'] = (tweets_df.sort_values('date')['date'].transform(lambda x: (x.diff() > '00:05:00').cumsum()))

# create a list of 5 min intervals from the start of df
start = tweets_df.iloc[0,'date']
end = tweets_df.iloc[-1, 'date']
interval = (end-start)

# delta = datetime.datetime.strptime(minutes = 5)
# end = datetime.datetime.strptime()

if __name__ == '__main__':
    x = start, end, interval
    print(x)