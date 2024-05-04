import requests

'''response = requests.get('http://google.com')
print(response.text)'''

'''url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "Dev",
    "body" : "bhai",
    "userId" : 1
}
headers = {'Content-Type': 'application/json; charset-UTF-8' }

response = requests.post(url, headers= headers, json= data)

print(response.text)'''

url = 'https://www.codewithharry.com/tutorial/react-home/'
r = requests.get(url)
# print(r.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, features="html.parser")

for heading in soup.find_all('p'):
    print(heading.text)