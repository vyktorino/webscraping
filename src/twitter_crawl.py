import twint
import pandas as pd


class TwitterCrawl:
    def __init__(self):
        pass

    def get_scrape(self) -> pd.DataFrame:
        """Returns the dataframe from the scrape

        Args:
            None

        Returns:
            scrape_df (pd.DataFrame): scraped dataframe with keep columns
        """

        c = twint.Config()

        topic_for_search = ["Rénovation énergétique"]
        c.Search = topic_for_search
        c.Limit = 100  # number of Tweets to scrape
        c.Lang = "fr"

        c.Pandas = True
        c.Hide_output = True
        # c.Near = "Paris"

        twint.run.Search(c)


def column_names():
    return twint.output.panda.Tweets_df.columns


def twint_to_pd(columns):
    return twint.output.panda.Tweets_df[columns]


keep_columns = ["id", "date", "place", "near", "geo"]
data = twint_to_pd(keep_columns)
print(data.head())


# tweets_df = twint.storage.panda.Tweets_df
# print(tweets_df.columns)
