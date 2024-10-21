from webscraping import Webscraping
import os
from dotenv import load_dotenv


load_dotenv()
google_form_link = os.getenv('Link_form')
zillow_link = "https://appbrewery.github.io/Zillow-Clone/"


scraping = Webscraping(zillow_link)

scraping.webscrape()
scraping.fill_in(google_form_link)

