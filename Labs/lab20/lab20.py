# *WRITE YOUR CODE IN THIS FILE*
from urllib import parse
import requests
import bs4


def get_domain(url):
    scheme = parse.urlparse(url).scheme
    if scheme == 'https' or scheme == 'http':
        domain = parse.urlparse(url).netloc
        return scheme + '://' + domain
    else:
        return ''


def combine_paths(url1, url2):
    return parse.urljoin(url1, url2)


def combine_urls(url1, url2):
    return parse.urljoin(url1, url2)


def print_pages(url, lst, output_file):
    with open(output_file, 'w') as f:
        for page in lst:
            # r = requests.get(combine_paths(url, page))
            # soup = str(bs4.BeautifulSoup(r.text, 'html.parser'))
            # f.write(soup)
            if page[0] == '/':
                r = requests.get(combine_paths(url, page))
                current_path = combine_paths(url, page)
            else:
                r = requests.get(combine_paths(current_path, page))
            soup = bs4.BeautifulSoup(r.text, 'html.parser')
            f.write(soup.string + '\n')
