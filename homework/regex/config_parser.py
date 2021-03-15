import re

PATH = "config.ini"
PATTERNS = [
    r'key": "(?P<id>[\w\@|.]+[^\"])',
    r'key = (?P<key>[\w\-]+)',
    r'password = (?P<pass>[\w]+)'
]
PATTERN_FOR_REPLACE = "*******"


def get_text(path) -> str:
    with open(path) as config_file:
        text = config_file.read()
    return text


def replace_patterns(text):
    for pattern in PATTERNS:
        res = re.findall(pattern, text, flags=re.M)
        text = re.sub(res[0], PATTERN_FOR_REPLACE, text)
    return text


def parse(path):
    text = get_text(path)
    res = replace_patterns(text)
    return res


if __name__ == "__main__":
    print(parse(PATH))
