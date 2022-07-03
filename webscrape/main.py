import pandas as pd

from twitter_scrape import ClassTwitterScrape
Scrape = ClassTwitterScrape()

tweets_df = Scrape.fetch_dataframe()

tweets_df['session'] = (tweets_df.sort_values('date')['time'].transform(lambda x: (x.diff() > '00:02:00').cumsum()))


if __name__ == '__main__':
    print(tweets_df.shape)