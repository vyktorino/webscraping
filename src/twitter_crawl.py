import datetime

import pytz
import twint
import pandas as pd

from pytz import timezone
from datetime import datetime as dt

from webscraping.src.database import host_engine


class ClassTwitterCrawl:
    def __init__(self):
        pass

    def webscrape(self) -> pd.DataFrame:
        """Returns the dataframe from the scrape

        Args:
            None

        Returns:
            scrape_df (pd.DataFrame): scraped dataframe with keep columns
        """

        c = twint.Config()

        topic_for_search = ["Rénovation énergétique"]
        c.Search = topic_for_search

        # Time
        eu_paris = timezone("Europe/Paris")
        paris_time = dt.now(eu_paris)

        today = dt.utcnow().date()  # current date and time
        c.Since = paris_time.strftime("%Y-%m-%d")

        c.Limit = 10  # number of Tweets to scrape
        c.Lang = "fr"
        c.Pandas = True
        c.Hide_output = True
        # c.Near = "Paris"

        twint.run.Search(c)

        keep_columns = ["id", "date", "place", "tweet"]

        webscrape_df = twint.output.panda.Tweets_df[keep_columns]

        return webscrape_df

    # def scrape_to_sql(self, scrape_df: pd.DataFrame) -> None:
    #     """Writes the data into the SQLAlchemy database

    #     Args:
    #         scrape_df (pd.DataFrame): output of the get_scrape method
    #     """
    #     return scrape_df.to_sql("Tweets", host_engine.engine)

    # def fetch_table(self) -> pd.DataFrame:
    #     """Returns the dataframe from the database via the connexion

    #     Returns:
    #         pd.DataFrame: processed dataframe fetched from the database
    #     """
    #     return pd.read_sql("select * from Tweets", host_engine.engine)


if __name__ == "__main__":
    Crawl = ClassTwitterCrawl()
    data = Crawl.webscrape()
    print(data)
