import re

PATH = "config.ini"
PATTERNS = [
    r'key": "(?P<id>[\w\@|.]+[^\"])',
    r'key = (?P<key>[\w\-]+)',
    r'password = (?P<pass>[\w]+)'
]
PATTERN_FOR_REPLACE = "*******"


def parse(path) -> str:
    with open(path) as config_file:
        text = config_file.read()
        for pattern in PATTERNS:
            res = re.findall(pattern, text, flags=re.M)
            text = re.sub(res[0], PATTERN_FOR_REPLACE, text)
        return text


if __name__ == "__main__":
    print(parse(PATH))
