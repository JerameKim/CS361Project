from bs4 import BeautifulSoup
import requests

# html_text has the response data, (<Response [200]>)
# html_text = requests.get('https://en.wikipedia.org/wiki/Lexus_F')

# get HTML from website
html_text = requests.get('https://en.wikipedia.org/wiki/Lexus_F').text

soup = BeautifulSoup(html_text, 'lxml')

print(html_text)

