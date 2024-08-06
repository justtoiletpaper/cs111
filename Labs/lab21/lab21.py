import requests, bs4, sys


def main():
    url = sys.argv[1]
    tag = sys.argv[2]
    attr = sys.argv[3]
    output = sys.argv[4]

    def scavenge(cur_url, cur_tag, cur_attr):
        r = requests.get(cur_url)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        obj = soup.find(f'<{cur_tag}>', f'<{cur_attr}>=True')
        if cur_attr == 'final':
            return obj.final.string
        else:
            txt = obj.cur_tag.attrs[cur_attr]
            lst = txt.split(',')
            url = lst[0]
            tag = lst[1]
            attr = lst[2]
            scavenge(url, tag, attr)
    file_content = scavenge(url, tag, attr)
    print(file_content)


if __name__ == '__main__':
    main()


