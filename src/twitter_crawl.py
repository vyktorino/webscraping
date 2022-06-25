import twint
import pandas as pd

c = twint.Config()

c.Search = ['Rénovation énergétique']       # topic
c.Limit = 100      # number of Tweets to scrape
c.Lang ="fr"


c.Pandas = True
c.Hide_output = True
# c.Near = "Paris"
# c.Store_csv = True       # store tweets in a csv file
# c.Output = "renov.csv"     # path to csv file

twint.run.Search(c)

def column_names():
  return twint.output.panda.Tweets_df.columns

def twint_to_pd(columns):
  return twint.output.panda.Tweets_df[columns]

keep_columns = ["id","date","place","near","geo"]
data = twint_to_pd(keep_columns)
print(data.head())


# tweets_df = twint.storage.panda.Tweets_df
# print(tweets_df.columns)