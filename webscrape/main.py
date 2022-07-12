import pandas as pd
from flask import Flask
from src.twitter_scrape import ClassTwitterScrape


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Flask!"


if __name__ == '__main__':
    Scrape = ClassTwitterScrape()

    tweets_df = Scrape.fetch_dataframe()

    tweets_df['date'] = pd.to_datetime(tweets_df['date'])
    # create a session for every 5 min
    # tweets_df['session'] = (tweets_df.sort_values('date')['date'].transform(lambda x: (x.diff() > '00:05:00').cumsum()))

    # create a list of 5 min intervals from the start of df
    start = tweets_df.iloc[0, 'date']
    end = tweets_df.iloc[-1, 'date']
    interval = (end - start)

    x = start, end, interval
    print(x)
    app.run(host="127.0.0.1", port=8080, debug=True)

