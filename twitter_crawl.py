import twint
import pandas as pd

c = twint.Config()

c.Search = ['Rénovation énergétique']       # topic
c.Limit = 50      # number of Tweets to scrape
c.Near = "Paris"
# c.Store_csv = True       # store tweets in a csv file
# c.Output = "renov.csv"     # path to csv file

twint.run.Search(c)

tweets_df = twint.storage.panda.Tweets_df
tweets_df.head(1)