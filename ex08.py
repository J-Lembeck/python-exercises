import requests
from bs4 import BeautifulSoup

url = 'http://github.com/'
r = requests.get(url)
raw_html = r.text

soup = BeautifulSoup(raw_html, 'html.parser')

article_titles = soup.find_all('h3')

print(":")
for title in article_titles:
    print(title.text)
