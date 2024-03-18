import requests
from bs4 import BeautifulSoup
import re

url = 'https://autazeszwajcarii.pl/aukcje/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', href=re.compile(r'/aukcje/licytacja/'))

processed_links = set()

with open("unique_links.txt", "w") as file:
    for link in links:
        href = link['href']
        if href not in processed_links:
            processed_links.add(href)
            file.write(href + '\n')

