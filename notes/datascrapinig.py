import requests
import bs4

# r = requests.get('./txt.html')
with open('txt.html', 'r') as f:
    text = f.read()
soup = bs4.BeautifulSoup(text, 'html.parser')
tags1 = soup.find_all('table', id='degrees')
print(tags1)
headerList = soup.find_all('th')
print(headerList)

