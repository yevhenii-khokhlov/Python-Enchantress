import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint


URL = "http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_" \
      "%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8" \
      "%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1" \
      "%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1" \
      "%81%D0%B8%D1%82%D0%B5%D1%82%D1%83"
HEADERS = \
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'}
PATTERN = \
    r"(^([ ]+[\d]{1,2}\..(?P<title>[\w\,\ \.\-]+[\S])))|" \
    r"(?P<department>[\w\.\'\"\,\ \-]+)[\W]+(?P<email>([\w\.])*@([\w\.])*)"


def get_html_text(url) -> str:
    r = requests.get(url=url, headers=HEADERS)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f'Status_code is {r.status_code}')


def parse(url) -> dict:
    parsed = {}
    dep_emails = []

    text = get_html_text(url)
    soup = BeautifulSoup(text, 'html.parser')
    content = soup.find('div', class_='mw-content-ltr').text
    res = re.finditer(PATTERN, content, flags=re.M)

    for item in res:
        if item.group('title'):
            title = item.group('title')
            dep_emails = []
            continue
        email = item.group('email')
        department = item.group('department')
        dep_emails.append((department, email))
        parsed.update({title: dep_emails})
    return parsed


if __name__ == "__main__":
    par = parse(URL)
    pprint(par)
