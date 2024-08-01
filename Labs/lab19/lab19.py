import requests
import bs4


def download(url, output_filename):
    "*** YOUR CODE HERE ***"
    code = requests.get(url)
    with open(output_filename, 'w') as f:
        f.write(code.text)


def make_pretty(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")
    with open(output_filename, 'w') as f:
        f.write(soup_object.prettify())


def find_paragraphs(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")
    soup_p = soup_object.find_all('p')
    with open(output_filename, 'w') as f:
        for p in soup_p:
            f.write(str(p) + '\n')


def find_links(url, output_filename):
    "*** YOUR CODE HERE ***"
    r = requests.get(url)
    soup_object = bs4.BeautifulSoup(r.content, features="html.parser")
    soup_a = soup_object.find_all('a')
    soup_links = []
    for a in soup_a:
        href = a.get('href')
        soup_links.append(str(href))
    with open(output_filename, 'w') as f:
        for link in soup_links:
            f.write(link + '\n')
