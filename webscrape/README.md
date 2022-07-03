# webscraping

Crawl throught the net to collect information on some trends

## Initialisation

Scrape Twitter data with Python [Source 1](https://www.natasshaselvaraj.com/how-to-scrape-twitter/) 

## Configuration

1. [Download](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019) `Microsoft C++ Build Tools`, and select `C++` as language support
2. Install the `twint` module by: `pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint` ([source](https://github.com/twintproject/twint/issues/915#issuecomment-896612605))

## Project Structure

The project is currently structured into `src` and `notebooks` folders. In each directory, the scripts are classified into the functionality to which they contribute. 

## Functionalities:

1. Database creation for tweet storage from search
2. Spatial distribution of tweets
3. Time series of tweets
4. Thematize the tweets
   1. NLP : [Scraping tweet using twint and analyzing with NLP](https://medium.com/@pragya_paudyal/scraping-tweet-using-twint-and-analyzing-with-nlp-932e01ad5587)


Interesting [Using Twint for Twitter data gathering](https://medium.com/@michael45684568/using-twint-for-twitter-data-gathering-d7197a3d4ce1)