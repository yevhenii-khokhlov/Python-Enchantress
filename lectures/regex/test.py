import re


with open("jang.log") as log_file:
    pattern = r"(?P<status_code>[\d]{3}).(?P<bytes>[\d]+)$"
    res = re.findall(pattern, log_file.read(), flags=re.M)
    print(sum(int(b) for status, b in res))

print("end")
