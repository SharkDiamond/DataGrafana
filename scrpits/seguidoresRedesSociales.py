import requests
import csv
from bs4 import BeautifulSoup



page = requests.get("https://www.instagram.com/osnetwireless")

print(page)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)


# Instantiate the scraper objects 
#google = Profile('https://www.instagram.com/google/')
#google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
#google_hashtag = Hashtag('https://www.instagram.com/explore/tags/google/')

# Scrape their respective data 
#google.scrape()
#google_post.scrape()
#google_hashtag.scrape()

#print(google.followers)
#print(google_post['hashtags'])
#print(google_hashtag.amount_of_posts)
