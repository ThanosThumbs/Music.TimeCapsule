from bs4 import BeautifulSoup
import requests
# enter the date
date = input ("Which year would you like to travel to musically? Type date in this format YYYY-MM-DD:")
# requesting the page
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
page = response.text
# creating the soup object
soup = BeautifulSoup(response.text, 'html.parser')
#receiving all track titles using the ids
ids = soup.select("li #Title-of-a-story")
# appending all the tracks from the ids list
songs = [id.text.strip() for id in ids]

print(songs)
