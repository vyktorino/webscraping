import datetime

import pytz
import twint
import pandas as pd

from pytz import timezone
from datetime import datetime as dt
from datetime import date, timedelta

from topic_search import topic_for_search

from host_engine import engine


class ClassTwitterScrape:
    def __init__(self):
        pass

    def webscrape(self) -> None:
        """Webscrapes

        Args:
            None

        Returns:
            scrape_df (pd.DataFrame): scraped dataframe with keep columns
        """

        # create the config
        c = twint.Config()

        # defining the topic to be searched
        c.Search = topic_for_search

        # Time
        eu_paris = timezone("Europe/Paris")  # set Paris timezone
        week_ago = (dt.now(eu_paris) - timedelta(days=7)).strftime(
            "%Y-%m-%d"
        )  # today minus 7 days

        c.Since = week_ago  # researches up to a week ago until now

        c.Limit = 1000  # number of Tweets to scrape
        c.Lang = "fr"  # search for french text
        c.Pandas = True
        c.Hide_output = True

        twint.run.Search(c)

        webscrape_df = twint.output.panda.Tweets_df
        webscrape_df['date'] = pd.to_datetime(webscrape_df['date'])

        keep_columns = ["id", "user_id", "username", "date", "tweet"]
        webscrape_df[keep_columns].to_sql(
            "Tweets", engine, if_exists="append"
        )  # send new dataframe to sql engine

    def fetch_dataframe(self) -> pd.DataFrame():
        """Returns the dataframe accessed on SQL

        Args:
            None

        Returns:
            (pd.DataFrame) : Tweets dataframe from host.engine
        """

        return pd.read_sql("select * from Tweets", engine).drop(
            columns="index"
        )


if __name__ == "__main__":
    Scrape = ClassTwitterScrape()
    Scrape.webscrape()
