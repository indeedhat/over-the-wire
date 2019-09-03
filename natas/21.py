#/bin/python3
import requests

username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
ses = "nncij3lg7firsudplck5c9le03"
url = "http://natas21.natas.labs.overthewire.org"

response = requests.get(url, auth=(username, password), cookies=dict(PHPSESSID=ses))

print(response.text)

