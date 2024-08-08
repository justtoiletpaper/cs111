import requests, re
from urllib import parse


class RequestGuard:

    def __init__(self, url):
        self.url = url
        scheme = parse.urlparse(self.url).scheme
        netloc = parse.urlparse(self.url).netloc
        self.domain = scheme + '://' + netloc
        self.forbidden = self.parse_robots()

    def parse_robots(self):
        r = requests.get(f'{self.domain}/robots.txt')
        regex_search = re.findall(r'Disallow:.*', r.text)
        disallow_lst = []
        for path in regex_search:
            cropped = path.replace('Disallow: ', '')
            disallow_lst.append(cropped)
        return disallow_lst

    def can_follow_link(self, url):
        for path in self.forbidden:
            if bool(re.match(f'{self.domain + path}', url)):
                return False
        if not bool(re.match(f'{self.domain}', url)):
            return False
        else:
            return True

    def make_get_request(self, url, use_stream=False):
        if not self.can_follow_link(url):
            return None
        else:
            return requests.get(url, stream = use_stream)


if __name__ == "__main__":
    pass
