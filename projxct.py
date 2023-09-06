#Importing modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL fro scrapping the data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = []
#soup.fing_all('td') will scrape every element in the url's table as td in 
# HTML is 'table data'
data_iterator = iter(soup.find_all('td'))
# data_iterratpor is the iterator of the table
# This loop will keep repeating until there is data available in the iterator

while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
        data.append((
            country,
            confirmed,
            deaths, 
            continent
        ))
        #StopIteration exception is raised when there are no more elements left to iterate
        # through 
    except StopIteration:
        break
    # sOrt the data by the number of confirmed cases
data.sort(key = lambda row: row[1], reverse = True)
df = pd.DataFrame(data, columns = ['Country', 'Confirmed', 'Deaths', 'Continent'])
print(df[1:100])
