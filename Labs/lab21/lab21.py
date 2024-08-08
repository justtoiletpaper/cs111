import requests, bs4, sys, re


def main():
    url = sys.argv[1]
    tag = sys.argv[2]
    attr = sys.argv[3]
    output = sys.argv[4]

    def scavenge(cur_url, cur_tag, cur_attr):
        r = requests.get(cur_url)
        soup = bs4.BeautifulSoup(r.content, features='html.parser')
        print(soup)
        tag_lst = soup.find_all(cur_tag)
        print(tag_lst)
        for elem in tag_lst:
            if bool(re.search(cur_attr, str(elem))):
                txt = elem
        txt_cropped = txt.get(cur_attr)
        if cur_attr == 'final':
            print(txt_cropped)
            return txt_cropped
        lst = txt_cropped.split(',')
        url = lst[0]
        tag = lst[1]
        attr = lst[2]
        return scavenge(url, tag, attr)

    writeout = scavenge(url, tag, attr)
    print(writeout)
    with open(output, 'w') as f:
        f.write(writeout)



if __name__ == '__main__':
    main()


