import requests
from bs4 import BeautifulSoup

url = 'http://github.com/'
response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

h3_tags = soup.find_all('h3')

with open('hard-coded.txt', 'w') as file:
    for h3 in h3_tags:
        file.write(h3.get_text() + '\n')

print('Elementos h3 salvos em hard-coded.txt!')